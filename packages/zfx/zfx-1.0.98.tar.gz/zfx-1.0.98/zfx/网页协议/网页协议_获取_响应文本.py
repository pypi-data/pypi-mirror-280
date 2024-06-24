def 网页协议_获取_响应文本(响应对象, 是否打印=False):
    """
    获取响应的文本内容。

    参数:
        响应对象 (requests.Response): 服务器响应对象。
        是否打印 (bool, optional): 是否打印执行结果，默认为 False。

    返回:
        str: 响应的文本内容。如果响应为 None 或出现任何异常则返回空字符串。
    """
    try:
        if 响应对象 is not None:
            响应文本 = 响应对象.text
            if 是否打印:
                print(f"响应的文本内容:\n{响应文本}")
            return 响应文本
        else:
            if 是否打印:
                print("响应对象为 None")
            return ''
    except Exception as e:
        if 是否打印:
            print(f"获取响应文本内容时出现异常: {e}")
        return ''