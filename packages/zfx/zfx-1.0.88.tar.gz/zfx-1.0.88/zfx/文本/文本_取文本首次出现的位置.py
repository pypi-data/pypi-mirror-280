def 文本_取文本首次出现的位置(文本, 查找的文本):
    """
    返回指定文本中指定子串首次出现的位置。

    参数：
    文本 (str): 要搜索的文本。
    查找的文本 (str): 要查找的子串。

    返回值：
    int: 子串首次出现的位置索引，如果没有找到返回-1。
    """
    try:
        # 使用find函数查找子串首次出现的位置
        首次位置 = 文本.find(查找的文本)
        return 首次位置
    except Exception:
        return -1