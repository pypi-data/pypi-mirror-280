import requests


def 网页协议_发送_GET请求(网址, 参数=None):
    """
    发送 GET 请求并返回服务器响应对象。

    参数:
        网址 (str): 请求的 URL。
        参数 (dict, optional): 要发送的参数，字典形式，默认为 None。

    返回:
        响应对象: 服务器响应对象。如果请求失败则返回 None。
    """
    try:
        响应 = requests.get(网址, params=参数)
        return 响应
    except Exception:
        return None