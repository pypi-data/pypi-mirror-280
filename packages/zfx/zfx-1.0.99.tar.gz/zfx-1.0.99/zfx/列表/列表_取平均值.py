def 列表_取平均值(列表):
    """
    返回列表中所有元素的平均值。

    参数:
        列表 (list): 包含数字的列表。

    返回:
        数值: 列表中所有元素的平均值。

    示例:
        平均值 = 列表_取平均值([1, 2, 3])
        if 平均值 is not None:
            print("列表元素的平均值:", 平均值)
        else:
            print("计算平均值失败")
    """
    try:
        if not 列表:
            return None
        return sum(列表) / len(列表)
    except Exception:
        return None