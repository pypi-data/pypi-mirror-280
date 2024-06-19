import math


def 算数_求正切(角度):
    """
    计算给定角度的正切值。

    参数:
    - 角度 (float): 要计算正切值的角度，单位为度。

    # 示例用法
    angle = 45
    tan_value = 算数_求正切(angle)
    print(f"{angle}度的正切值为: {tan_value}")

    返回:
    - 正切值 (float): 给定角度的正切值。
    """
    # 将角度转换为弧度
    弧度 = math.radians(角度)

    # 计算正切值
    正切值 = math.tan(弧度)

    return 正切值



