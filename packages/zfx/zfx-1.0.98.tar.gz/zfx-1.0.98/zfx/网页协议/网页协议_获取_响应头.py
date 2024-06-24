def 网页协议_获取_响应头(响应对象, 是否打印=False):
    """
    获取响应头的字典形式。

    参数:
        响应对象 (requests.Response): 服务器响应对象。
        是否打印 (bool, optional): 是否打印执行结果，默认为 False。

    返回:
        dict: 响应头的字典形式。如果响应为 None 或出现任何异常则返回空字典。
    """
    try:
        if 响应对象 is not None:
            响应头 = 响应对象.headers
            if 是否打印:
                print("响应头:")
            return 响应头
        else:
            if 是否打印:
                print("响应对象为 None")
            return {}
    except Exception as e:
        if 是否打印:
            print(f"获取响应头时出现异常: {e}")
        return {}
