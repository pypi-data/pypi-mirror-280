import asyncio
import logging
import threading
import time
from collections import deque
from pathlib import Path
from threading import Thread
from typing import Callable

import httpx

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] <%(name)s> [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(),
    ],
)


class _DynamicSemaphore:
    def __init__(self, initial_permits):
        self._permits = initial_permits
        self._semaphore = asyncio.Semaphore(initial_permits)
        self._lock = asyncio.Lock()

    async def acquire(self):
        await self._semaphore.acquire()

    def release(self):
        self._semaphore.release()

    async def set_permits(self, permits):
        async with self._lock:
            difference = permits - self._permits
            if difference > 0:
                for _ in range(difference):
                    self._semaphore.release()
            elif difference < 0:
                for _ in range(-difference):
                    await self._semaphore.acquire()
            self._permits = permits

    async def adjust_concurrency(self, concurrency: float, last_concurrency: float):
        slot = self._permits
        if concurrency > last_concurrency:
            slot = max(1, self._permits - 1)
        elif concurrency < last_concurrency:
            slot += 1
        logger.info(f"dynamic concurrency {self._permits}[{last_concurrency}] --> {slot}[{concurrency}]")
        if slot == self._permits: return
        await self.set_permits(slot)

    def get_permits(self):
        return self._permits


class YunDownloader:
    CHUNK_SIZE = 100 * 1024 * 1024
    HEARTBEAT_SLEEP = 5
    DISTINGUISH_SIZE = 500 * 1024 * 1024

    def __init__(self, url: str, save_path: str, limit: int = 16, dynamic_concurrency: bool = False,
                 update_callable: Callable = None, params: dict = None, timeout: int = 200, headers: dict = None,
                 cookies: dict = None):
        """
        初始化下载器对象。

        :param url: 需要下载的资源的URL。
        :param save_path: 下载资源的保存路径。
        :param limit: 并发下载资源的最大数量，默认为16。
        :param dynamic_concurrency: 是否启用动态并发下载，默认为False。
        :param update_callable: 一个可调用对象，用于在下载过程中更新进度等信息。
        :param params: 用于URL查询字符串的参数字典。
        :param timeout: 连接和读取操作的超时时间，默认为200秒。
        :param headers: HTTP请求头字典，用于自定义请求头。
        :param cookies: cookies字典，用于在请求中包含cookies。
        """
        # 保存更新回调函数的引用
        self.__update_callable = update_callable
        # 初始化事件循环变量，默认为None
        self.loop: asyncio.AbstractEventLoop | None = None
        self.semaphore = _DynamicSemaphore(limit)
        # 保存资源的URL
        self.url = url
        # 将保存路径转换为Path对象，并确保其父目录存在
        self.save_path = Path(save_path)
        self.save_path.parent.mkdir(exist_ok=True, parents=True)
        # 保存超时时间
        self.timeout = timeout
        # 保存请求头，默认为空字典
        self.headers = headers if headers else {}
        # 保存cookies
        self.cookies = cookies
        # 保存请求参数
        self.params = params
        # 初始化断点续传标志
        self.is_breakpoint = False
        # 初始化内容长度
        self.content_length = None
        # 初始化下载计数
        self.download_count = 0
        # 初始化上次计数
        self.last_count = 0
        # 记录下载开始时间
        self.start_time = time.time()
        # 动态并发
        self._dynamic_concurrency = dynamic_concurrency
        # 响应时间存储
        self._response_time_deque = deque(maxlen=10)
        self._last_concurrency = -1

    def check_breakpoint(self):
        """
        检查下载是否可以从断点处继续。

        使用httpx客户端发起HTTP请求，首先通过HEAD请求获取资源的Content-Length，然后通过GET请求检查服务器是否支持断点续传。

        如果资源的Content-Length可获取且服务器支持断点续传，则设置断点续传标志为True，并记录资源的长度。
        """
        # 使用httpx客户端，配置超时、请求头、cookies等参数
        with httpx.Client(
                timeout=self.timeout,
                headers=self.headers,
                cookies=self.cookies,
                params=self.params,
                transport=httpx.HTTPTransport(retries=5),
                follow_redirects=True) as client:
            try:
                # 发起HEAD请求，获取资源的元信息
                content_res = client.head(self.url, timeout=self.timeout, headers=self.headers, cookies=self.cookies)
                content_res.raise_for_status()
                # 尝试获取资源的Content-Length，如果不可用则返回，不支持断点续传
                content_length = int(content_res.headers.get('content-length', -1))
                if content_length == -1: return

                # 发起GET请求，检查服务器是否支持断点续传
                res = client.get(self.url, headers={'Range': 'bytes=0-1'})
                # 如果服务器返回的状态码不是206，则不支持断点续传，返回
                if res.status_code != 206: return

                # 如果一切检查通过，设置断点续传标志为True，并记录资源长度
                self.is_breakpoint = True
                self.content_length = content_length
            except Exception as e:
                # 记录检查断点续传时发生的异常
                logger.error(f'{self.url} check breakpoint error: {e}')

    def select_downloader(self):
        """
        根据文件大小和是否存在选择合适的下载方式。

        如果文件已存在且大小正确，则不进行下载。否则，根据文件大小选择分块下载或流式下载。
        对于大于100MB的文件，且支持断点续传，使用分块下载；否则，使用流式下载。
        """
        # 检查目标文件是否已存在且大小正确，如果满足条件，则不进行下载
        if self.save_path.exists() and self.save_path.stat().st_size == self.content_length:
            logger.info(f'{self.url} file exists and size correct, skip download')
            return

        # 初始化异步事件循环
        self.loop = asyncio.new_event_loop()

        # 对于大于DISTINGUISH_SIZE的文件，且支持断点续传，选择分块下载
        if self.content_length is not None and self.content_length > self.DISTINGUISH_SIZE and self.is_breakpoint:
            # 大文件分块下载
            logger.info(f'{self.url} select slice download')
            self.loop.run_until_complete(self.slice_download())
        else:
            # 对于小文件或不支持断点续传的文件，选择流式下载
            # 小文件流下载
            logger.info(f'{self.url} select stream download')
            stop_event = threading.Event()
            t = Thread(target=lambda: self.heartbeat_t(stop_event), daemon=True)
            t.start()
            self.stream_download()
            stop_event.set()
            t.join()
        self.loop.close()

    async def chunk_download(self, semaphore: _DynamicSemaphore, client: httpx.AsyncClient, chunk_start: int,
                             chunk_end: int, save_path: Path):
        """
        异步下载文件的一个片段。

        检查片段是否已存在并完全下载，如果存在则跳过下载。
        如果片段不存在或不完整，则从服务器请求该片段并将其写入文件。

        参数:
        client: httpx.AsyncClient实例，用于发送HTTP请求。
        chunk_start: 片段的起始字节位置。
        chunk_end: 片段的结束字节位置。
        save_path: 文件的保存路径。

        返回:
        True: 如果片段成功下载或已存在。
        False: 如果下载过程中发生错误。
        """
        await semaphore.acquire()
        # 检查片段是否已完全下载，如果是，则跳过下载
        headers = {'Range': f'bytes={chunk_start}-{chunk_end}'}
        if save_path.exists():
            if save_path.stat().st_size == (chunk_end - chunk_start + 1):
                logger.info(f'{save_path} chunk {chunk_start}-{chunk_end} skip')
                self.download_count += (chunk_end - chunk_start + 1)
                semaphore.release()
                return True
            headers['Range'] = f'bytes={chunk_start + save_path.stat().st_size}-{chunk_end}'

        # 使用异步客户端发送GET请求，并流式处理响应的字节数据
        async with client.stream('GET', self.url, headers=headers) as res:
            try:
                # 确保响应状态码正常
                res.raise_for_status()
                # 打开文件并写入响应的字节数据
                with save_path.open('ab') as f:
                    async for chunk in res.aiter_bytes(chunk_size=2048):
                        f.write(chunk)
                        res: httpx.Response
                        self.download_count += len(chunk)
                    self._response_time_deque.append(res.elapsed.seconds)
                return True
            except Exception as e:
                logger.error(f'{save_path} chunk download error: {e}')
                return False
            finally:
                semaphore.release()

    async def slice_download(self):
        """
        异步下载大文件的切片。

        该方法首先启动一个心跳任务以保持连接 alive，然后使用 httpx 创建一个异步客户端来处理文件的切片下载。
        下载过程中，文件被分成多个切片，并同时下载这些切片以提高效率。所有切片下载完成后，会将它们合并成原始文件。
        """

        # 启动一个心跳任务，以保持连接 alive
        # noinspection PyAsyncCall
        ping = self.loop.create_task(self.heartbeat())

        # 使用 httpx 创建异步客户端，配置超时、请求头、cookies、参数等
        async with httpx.AsyncClient(
                timeout=self.timeout,
                headers=self.headers,
                cookies=self.cookies,
                params=self.params,
                transport=httpx.AsyncHTTPTransport(retries=5),
                follow_redirects=True,
                limits=httpx.Limits(max_connections=16, max_keepalive_connections=16),
                max_redirects=5) as client:

            # 初始化任务列表，用于存储所有切片下载任务
            tasks = []

            # 遍历文件切片，为每个切片创建一个下载任务
            for index, chunk_start in enumerate(range(0, self.content_length, self.CHUNK_SIZE)):
                chunk_end = min(chunk_start + self.CHUNK_SIZE - 1, self.content_length)
                save_path = self.save_path.parent / '{}--{}.distributeddownloader'.format(
                    self.save_path.stem, str(index).zfill(5))

                # 记录日志，显示当前切片的下载信息
                logger.info(f'{self.url} slice download {index} {chunk_start} {chunk_end}')
                # 创建下载任务，并将其添加到任务列表
                tasks.append(self.loop.create_task(
                    self.chunk_download(self.semaphore, client, chunk_start, chunk_end, save_path)))

            # 并发执行所有下载任务
            tasks = await asyncio.gather(*tasks)
            ping.cancel()
            # 检查所有下载任务是否成功完成
            if all(tasks):
                # 所有切片下载成功，进行切片合并
                logger.info(f'{self.save_path} Download all slice success')
                merge_state = await self.merge_chunk()

                # 如果切片合并失败，则抛出异常
                if not merge_state:
                    raise Exception(f'{self.save_path} Merge all slice error')
                logger.info(f'Success download file, run time: {int(time.time() - self.start_time)} S')
            else:
                # 如果有任何切片下载失败，则抛出异常
                logger.error(f'{self.save_path} Download all slice error')
                raise Exception(f'{self.save_path} Download all slice error')

    async def merge_chunk(self):
        """
        合并下载的分片文件。

        找到所有匹配的分片文件，按序读取每个分片文件的内容，并写入到最终的目标文件中。
        合并完成后，删除所有的分片文件。

        Returns:
            bool: 返回True表示合并成功，返回False表示合并失败。
        """
        # 使用glob模式匹配所有分片文件
        slice_files = list(self.save_path.parent.glob(f'*{self.save_path.stem}*.distributeddownloader'))
        # 根据分片文件名中的序号对文件进行排序
        slice_files.sort(key=lambda x: int(x.stem.split('--')[1]))

        try:
            # 打开目标文件，以二进制写入模式准备写入合并后的内容
            with self.save_path.open('wb') as wf:
                # 遍历所有分片文件
                for slice_file in slice_files:
                    # 以二进制读取模式打开分片文件
                    with slice_file.open('rb') as rf:
                        # 不断读取分片文件的内容，直到读取完毕
                        while True:
                            chunk = rf.read(4096)
                            # 如果读取到的块为空，则表示读取完毕，退出循环
                            if not chunk:
                                break
                            # 将读取到的块写入到目标文件中
                            wf.write(chunk)

            # 删除所有的分片文件
            for slice_file in slice_files:
                slice_file.unlink()

            # 记录日志，表示文件合并成功
            logger.info(f'{self.save_path} merge chunk success')
            return True
        except Exception as e:
            # 记录日志，表示文件合并失败，并记录错误信息
            logger.error(f'{self.save_path} merge chunk error: {e}')
            return False

    def stream_download(self):
        """
        使用httpx库进行流式下载文件。

        本方法支持断点续传下载，如果下载中断，再次启动时会从上次中断的位置继续下载。
        使用了httpx的Client进行HTTP请求，并配置了超时时间、请求头、cookies和重试机制。

        如果是断点续传下载，会根据已保存文件的大小设置Range请求头，以继续下载剩余部分。
        如果不是断点续传，或者文件大小未知，则会重新下载整个文件，并覆盖已有的文件。

        在下载过程中，会捕获任何异常，并记录错误日志，然后重新抛出异常。
        """
        # 使用httpx的Client来发起HTTP请求，并配置超时、请求头、cookies和重试次数
        with httpx.Client(
                timeout=self.timeout,
                headers=self.headers,
                cookies=self.cookies,
                transport=httpx.HTTPTransport(retries=5)) as client:
            headers = {}
            # 如果支持断点续传且已知文件总长度
            if self.is_breakpoint and self.content_length is not None:
                # 如果保存路径存在，则设置Range请求头，从已下载的大小开始继续下载
                if self.save_path.exists():
                    self.headers['Range'] = f'bytes={self.save_path.stat().st_size + 1}-'
                    self.download_count = self.save_path.stat().st_size
                    logger.info(f'{self.url} breakpoint download')
            else:
                # 如果不支持断点续传，或文件长度未知，则删除已存在的目标文件
                self.save_path.unlink(missing_ok=True)
            # 使用stream方法进行GET请求，以流式处理响应
            with client.stream('GET', self.url, headers=headers) as res:
                try:
                    # 检查响应状态码，如果不正常则抛出异常
                    res.raise_for_status()
                    # 以追加写模式打开目标文件，用于写入下载的文件内容
                    with self.save_path.open('ab+') as f:
                        # 通过iter_bytes方法以指定大小的块遍历响应内容，并写入文件
                        for chunk in res.iter_bytes(chunk_size=2048):
                            f.write(chunk)
                            self.download_count += len(chunk)
                except Exception as e:
                    # 记录下载过程中的异常错误日志，并重新抛出异常
                    logger.error(f'{self.url} stream download error: {e}')
                    raise e

    async def heartbeat(self):
        """
        心跳函数，用于定期报告下载进度和速度。

        此函数是一个异步函数，它在后台运行，不会阻塞其他操作。它定期计算下载进度和速度，
        并调用一个指定的回调函数来更新状态。如果下载被取消，它会优雅地退出。
        """
        try:
            # 无限循环，直到任务被取消
            while True:
                # 暂停一段时间后继续，模拟心跳间隔
                await asyncio.sleep(self.HEARTBEAT_SLEEP)

                # 如果下载计数为0，跳过本次循环，不进行进度更新
                if self.download_count == 0:
                    logger.info(f'{self.url} heartbeat: wait download')
                    continue

                # 计算下载进度，如果总长度未知，则设为-1
                progress = (self.download_count / self.content_length) if self.content_length is not None else -1

                # 计算下载速度，单位为MB/S
                speed = (self.download_count - self.last_count) / 1048576 / self.HEARTBEAT_SLEEP

                # 如果存在更新回调函数，则调用它来更新下载状态
                if self.__update_callable:
                    self.__update_callable(
                        state='PROGRESS',
                        meta={
                            'progress': progress,
                            'speed': speed,
                            'run_time': self.start_time
                        })
                average_concurrency = sum(self._response_time_deque) / len(self._response_time_deque) if len(
                    self._response_time_deque) else None
                logger.info(f'{self.url} '
                            f'heartbeat: {progress * 100:.2f} '
                            f'run_time: {int(time.time() - self.start_time)} '
                            f'speed: {speed:.2f} MB/S '
                            f'response_time: {average_concurrency} '
                            f'download_size: {self.download_count / 1048576:.2f} MB')

                if self._last_concurrency != -1 and self._dynamic_concurrency:
                    await self.semaphore.adjust_concurrency(average_concurrency, self._last_concurrency)
                if average_concurrency is not None:
                    self._last_concurrency = average_concurrency

                # 更新上次下载计数，用于下次计算速度
                self.last_count = self.download_count
        except Exception as e:
            # 如果任务被取消，打印信息并优雅退出
            logger.warning("Task is cancelling...")
            # 清理资源
            return

    def heartbeat_t(self, stop_event):
        """
        心跳函数，用于定期报告下载进度和速度。

        此函数是一个异步函数，它在后台运行，不会阻塞其他操作。它定期计算下载进度和速度，
        并调用一个指定的回调函数来更新状态。如果下载被取消，它会优雅地退出。
        """
        try:
            # 无限循环，直到任务被取消
            while not stop_event.is_set():
                # 暂停一段时间后继续，模拟心跳间隔
                time.sleep(self.HEARTBEAT_SLEEP)

                # 如果下载计数为0，跳过本次循环，不进行进度更新
                if self.download_count == 0:
                    logger.info(f'{self.url} heartbeat: wait download')
                    continue

                # 计算下载进度，如果总长度未知，则设为-1
                progress = (self.download_count / self.content_length) if self.content_length is not None else -1

                # 计算下载速度，单位为MB/S
                speed = (self.download_count - self.last_count) / 1048576 / self.HEARTBEAT_SLEEP

                # 如果存在更新回调函数，则调用它来更新下载状态
                if self.__update_callable:
                    self.__update_callable(
                        state='PROGRESS',
                        meta={
                            'progress': progress,
                            'speed': speed,
                            'run_time': self.start_time
                        })
                logger.info(f'{self.url} heartbeat: {progress * 100:.2f} speed: {speed:.2f} MB/S')

                # 更新上次下载计数，用于下次计算速度
                self.last_count = self.download_count
        except asyncio.CancelledError:
            # 如果任务被取消，打印信息并优雅退出
            print("Task is cancelling...")
            # 清理资源
            return

    def workflow(self):
        """
        执行下载工作的流程控制方法。

        本方法负责初始化下载计数器，检查下载是否需要从断点继续，并选择合适的下载器。
        它不接受任何参数，也没有返回值，通过直接修改对象状态来推动下载流程的进行。
        """
        logger.info(f'{self.url} workflow start')
        # 初始化下载计数器
        self.download_count = 0
        # 检查下载任务是否需要从断点继续
        self.check_breakpoint()
        # 根据当前条件选择合适的下载器
        self.select_downloader()

    def run(self, error_retry: int | bool = False):
        if isinstance(error_retry, int) and error_retry > 0:
            flag = 0
            while True:
                try:
                    self.workflow()
                    break
                except Exception as e:
                    logger.error(f'{self.url} download error: {e}')
                    flag += 1
                    if flag >= error_retry:
                        logger.warning(f'{self.url} download retry skip: {e}')
                        break
        else:
            self.workflow()
