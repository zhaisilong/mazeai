import time
from loguru import logger
from maze.utils import OrderedTaskProcessor

def example_task(n):
    try:
        logger.info(f"Processing task: {n}")
        time.sleep(0.5)
        result = n * n
        logger.info(f"Task {n} completed with result: {result}")
        if n == 5:
            raise Exception("Task 5 failed")
        return result
    except Exception as e:
        logger.error(f"Task {n} failed with error: {e}")

def main():

    # 配置日志
    logger.add("task_processor.log", rotation="500 KB", level="INFO")

    # 配置任务参数
    task_args = list(range(10))  # 任务参数列表
    num_processes = 4  # 进程池大小

    # 初始化任务处理器
    processor = OrderedTaskProcessor(example_task, num_processes=num_processes)

    # 执行任务
    results = processor.execute_tasks(task_args)

    # 输出结果
    logger.info(f"Final results (ordered): {results}")


if __name__ == "__main__":
    main()