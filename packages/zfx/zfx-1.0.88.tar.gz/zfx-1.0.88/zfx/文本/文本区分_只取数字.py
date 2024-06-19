def 文本区分_只取数字(源文本):
    """
    # 示例用法
    源文本 = "这是一个示例文本，包含一些数字：1234567890"
    数字文本 = 文本区分_只取数字(源文本)
    print("提取的数字文本:", 数字文本)
    """
    # 使用正则表达式匹配数字
    数字列表 = ''.join(filter(str.isdigit, 源文本))
    return 数字列表