def 网页协议_获取_响应cookies(响应对象, 是否打印=False):
    """
    获取响应的 cookies。

    参数:
        响应对象 (requests.Response): 服务器响应对象。
        是否打印 (bool, optional): 是否打印执行结果，默认为 False。

    返回:
        响应的 cookies 对象。如果响应为 None 或出现任何异常则返回空的 字典。
    """
    try:
        if 响应对象 is not None:
            cookies = 响应对象.cookies
            if 是否打印:
                print(f"响应的 cookies: {cookies}")
            return cookies
        else:
            if 是否打印:
                print("响应对象为 None")
            return {}
    except Exception as e:
        if 是否打印:
            print(f"获取响应 cookies 时出现异常: {e}")
        return {}