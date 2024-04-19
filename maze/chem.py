# https://github.com/dan2097/opsin

from urllib.request import urlopen
from urllib.parse import quote  # 用于确保 URL 编码正确
from loguru import logger
from typing import Optional


def identifier_to_smiles(structure_identifier: str) -> Optional[str]:
    """将分子标志符转化成smiles

    Args:
        structure_identifier (str): 分子标志符

    Returns:
        str: smiles

    - [转化的网站](https://cactus.nci.nih.gov/chemical/structure)
    """
    # 对输入的结构标识符进行 URL 编码，以确保 URL 的正确性
    encoded_identifier = quote(structure_identifier)

    # 构建请求的 URL
    url = f"http://cactus.nci.nih.gov/chemical/structure/{encoded_identifier}/smiles"

    # 尝试打开 URL 并读取内容
    try:
        response = urlopen(url)
        smiles = response.read().decode("utf8")
        return smiles
    except Exception as e:
        logger.exception(f"发生错误: {e}")
        return None

if __name__ == "__main__":
    # 示例结构标识符，可以是 CAS 号码、化学名称等
    structure_identifier = 'Acetaminophen'  # 例如用药物的常用名
    # 调用函数并打印结果
    smiles = identifier_to_smiles(structure_identifier)
    print("Structure Identifier:", structure_identifier)
    print("SMILES Notation:", smiles)
