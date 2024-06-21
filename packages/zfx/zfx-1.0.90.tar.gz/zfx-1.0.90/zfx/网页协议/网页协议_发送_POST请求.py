import requests


def 网页协议_发送_POST请求(网址, 数据, 是否打印=False):
    """
    发送 POST 请求并返回服务器响应。

    参数:
        网址 (str): 请求的 URL。
        数据 (dict): 要发送的数据，字典形式。
        是否打印 (bool, optional): 是否打印执行结果，默认为 False。

    返回:
        str: 服务器响应的文本。如果请求失败则返回 None。
    """
    try:
        响应 = requests.post(网址, data=数据)
        if 是否打印:
            print(响应.text)
        return 响应.text
    except Exception as e:
        if 是否打印:
            print(f"请求异常: {e}")
        return None
