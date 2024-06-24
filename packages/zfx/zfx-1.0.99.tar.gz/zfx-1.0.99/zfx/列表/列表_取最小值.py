def 列表_取最小值(列表):
    """
    返回列表中的最小值。

    参数:
        列表 (list): 包含数字的列表。

    返回:
        数值: 列表中的最小值。如果列表为空，返回 None。

    示例:
        最小值 = 列表_取最小值([1, 2, 3])
        if 最小值 is not None:
            print("列表中的最小值:", 最小值)
        else:
            print("获取最小值失败")
    """
    try:
        if not 列表:
            return None
        return min(列表)
    except Exception:
        return None
