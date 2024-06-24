def 列表_取最大值(列表):
    """
    返回列表中的最大值。

    参数:
        列表 (list): 包含数字的列表。

    返回:
        数值: 列表中的最大值。如果列表为空，返回 None。

    示例:
        最大值 = 列表_取最大值([1, 2, 3])
        if 最大值 is not None:
            print("列表中的最大值:", 最大值)
        else:
            print("获取最大值失败")
    """
    try:
        if not 列表:
            return None
        return max(列表)
    except Exception:
        return None