def 网页协议_获取_响应文本去除换行符(响应对象, 是否打印=False):
    """
    获取响应的文本内容，并移除其中的换行符。

    参数:
        响应对象: 服务器响应对象。
        是否打印 (bool, optional): 是否打印执行结果，默认为 False。

    返回:
        str: 处理后的响应文本内容，所有换行符都被移除。如果响应为 None 或出现任何异常，则返回空字符串。
    """
    try:
        if 响应对象 is not None:
            文本内容 = 响应对象.text
            处理后文本 = 文本内容.replace('\n', '').replace('\r', '')  # 移除换行符
            if 是否打印:
                print(f"处理后的响应文本内容:\n{处理后文本}")
            return 处理后文本
        else:
            if 是否打印:
                print("响应对象为 None")
            return ''
    except Exception as e:
        if 是否打印:
            print(f"获取响应文本内容时出现异常: {e}")
        return ''