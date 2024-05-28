from typing import Optional, Union
from pathlib import Path

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

