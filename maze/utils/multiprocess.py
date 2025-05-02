from multiprocessing import Pool
import multiprocessing
import traceback

from loguru import logger
from tqdm import tqdm


class OrderedTaskProcessor:
    def __init__(self, task_function, num_processes=4, timeout=300):
        """task function 的最后一个参数是 shared_list"""
        self.task_function = task_function
        self.num_processes = num_processes
        self.timeout = timeout

    def execute_tasks(self, task_args):
        with Pool(processes=self.num_processes) as pool:
            results = []
            for arg in task_args:
                result = pool.apply_async(self.task_function, args=(arg,))
                results.append(result)
            # 收集结果，保持顺序
            ordered_results = []
            for result in tqdm(results, total=len(results), desc="Processing Tasks"):
                try:
                    res = result.get(timeout=self.timeout)
                    if res is None:
                        continue
                    ordered_results.append(res)
                except multiprocessing.TimeoutError:
                    logger.error(f"任务超时，超时时间为 {self.timeout} 秒。")
                    continue
                except Exception as e:
                    raise Exception(f"任务执行时发生异常: {e}\n{traceback.format_exc()}")
        return ordered_results

    def _wrapper_task(self, task_arg):
        self.task_function(task_arg)