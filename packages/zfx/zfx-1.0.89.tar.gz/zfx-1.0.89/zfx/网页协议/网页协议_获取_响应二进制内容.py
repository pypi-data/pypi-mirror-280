def 网页协议_获取_响应二进制内容(响应对象, 是否打印=False):
    """
    获取响应的二进制内容。

    参数:
        响应对象 (requests.Response): 服务器响应对象。
        是否打印 (bool, optional): 是否打印执行结果，默认为 False。

    返回:
        bytes: 响应的二进制内容。如果响应为 None 或出现任何异常则返回空字节串。
    """
    try:
        if 响应对象 is not None:
            响应内容 = 响应对象.content
            if 是否打印:
                print(f"响应的二进制内容: {响应内容}")
            return 响应内容
        else:
            if 是否打印:
                print("响应对象为 None")
            return b''
    except Exception as e:
        if 是否打印:
            print(f"获取响应二进制内容时出现异常: {e}")
        return b''
