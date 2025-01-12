from typing import Optional, Union
from pathlib import Path
import multiprocessing
from multiprocessing import Manager, Pool
from loguru import logger
from tqdm import tqdm
import traceback

def count_dir(directory: Union[str, Path], extensions: Optional[str]=None):
    """
    统计目录中文件的数量，基于指定的文件后缀名。

    Args:
    - directory (str): 目标目录路径
    - extensions (list): 允许的文件后缀名列表，如 ['.txt', '.csv']。
                         如果为空或 None，则统计所有文件。

    Returns:
    - None
    """
    # 创建或转换 Path 对象
    if isinstance(directory, Path):
        dir_path = directory
    elif isinstance(directory, str):
        dir_path = Path(directory)
    else:
        raise TypeError(f"参数 'directory' 必须是字符串或 pathlib.Path 对象，当前类型为 {type(directory)}。")

    # 检查是否为目录
    if not dir_path.is_dir():
        print(f"'{directory}' 不是有效的目录。")
        return

    # 使用生成器表达式获取符合条件的文件
    if extensions:
        files = [file for file in dir_path.iterdir() if file.is_file() and file.suffix.lower() in extensions]
    else:
        files = [file for file in dir_path.iterdir() if file.is_file()]

    # 统计文件数量
    return len(files)

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