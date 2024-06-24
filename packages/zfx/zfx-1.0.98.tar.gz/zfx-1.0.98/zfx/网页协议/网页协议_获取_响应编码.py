def 网页协议_获取_响应编码(响应对象, 是否打印=False):
    """
    获取响应的编码格式。

    参数:
        响应对象: 服务器响应对象。
        是否打印: 是否打印执行结果和异常信息，布尔值，默认为 False。

    返回:
        str: 响应的编码格式，如果响应为 None 或出现任何异常则返回空字符串。
    """
    try:
        if 响应对象 is not None:
            编码格式 = 响应对象.encoding
            if 是否打印:
                print(f"响应编码格式: {编码格式}")
            return 编码格式
        else:
            if 是否打印:
                print("响应对象为 None，无法获取编码格式")
            return ''
    except Exception as e:
        if 是否打印:
            print(f"获取响应编码时出现异常: {e}")
        return ''
