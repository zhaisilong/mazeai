import os
import requests
from typing import Optional, Tuple

from loguru import logger


def set_proxy(proxy_str: Optional[str] = None):
    """设置代理"""
    if not proxy_str:
        os.environ["http_proxy"] = "http://127.0.0.1:10809"
        os.environ["https_proxy"] = "https://127.0.0.1:10809"
    else:
        os.environ["http_proxy"] = proxy_str
        os.environ["https_proxy"] = proxy_str


def get_proxy() -> Tuple[str]:
    """获取代理"""
    try:
        return (os.environ["http_proxy"], os.environ["https_proxy"])
    except Exception as e:
        logger.warning(f"There was no proxy setted: {e}")
        return ("", "")
        

def unset_proxy():
    """取消代理设置"""
    os.environ["http_proxy"] = ""
    os.environ["https_proxy"] = ""


def fetch_url(url: str, proxy: bool = False) -> Optional[str]:
    """
    发起 GET 请求并返回响应内容或错误消息
    """
    try:
        origin_proxy = get_proxy()
        if proxy:
            origin_proxy = get_proxy()[0]
            set_proxy()
        # 发起 GET 请求
        response = requests.get(url)

        # 检查响应状态码
        if response.status_code == 200:
            # 返回响应内容
            return response.text
        else:
            logger.error(f"Failed to fetch URL: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error: {e}")
        return None
    finally:
        if proxy:
            logger.info("set proxy to orignal")
            set_proxy(origin_proxy)


if __name__ == "__main__":
    # 测试函数
    url_to_fetch = "https://www.google.com"
    result = fetch_url(url_to_fetch, proxy=True)
