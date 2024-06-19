def 网页协议_获取_响应文本取中间(响应对象, 文本前缀, 文本后缀):
    """
    获取响应的文本内容，并从中提取介于文本前缀和文本后缀之间的部分文本。

    参数:
        响应对象: 服务器响应对象。
        文本前缀: 前缀字符串，用于定位目标文本的起始位置。
        文本后缀: 后缀字符串，用于定位目标文本的结束位置。

    返回:
        str: 响应文本中位于文本前缀和文本后缀之间的部分文本。如果响应为 None、未找到匹配的文本、或出现任何异常，则返回空字符串。
    """
    try:
        if 响应对象 is not None:
            文本内容 = 响应对象.text
            起始位置 = 文本内容.find(文本前缀)
            if 起始位置 != -1:
                起始位置 += len(文本前缀)
                结束位置 = 文本内容.find(文本后缀, 起始位置)
                if 结束位置 != -1:
                    return 文本内容[起始位置:结束位置]
            return ''
        else:
            return ''
    except Exception:
        return ''