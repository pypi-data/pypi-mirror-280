def 网页协议_获取_HTTP状态码(响应对象, 是否打印=False):
    """
    获取 HTTP 状态码。

    参数:
        响应对象 (requests.Response): 服务器响应对象。
        是否打印 (bool, optional): 是否打印执行结果，默认为 False。

    返回:
        int: HTTP 状态码。如果响应为 None 或出现任何异常则返回 None。
    """
    try:
        if 响应对象 is not None:
            状态码 = 响应对象.status_code
            if 是否打印:
                print(f"HTTP 状态码: {状态码}")
            return 状态码
        else:
            if 是否打印:
                print("响应对象为 None")
            return None
    except Exception as e:
        if 是否打印:
            print(f"获取状态码时出现异常: {e}")
        return None