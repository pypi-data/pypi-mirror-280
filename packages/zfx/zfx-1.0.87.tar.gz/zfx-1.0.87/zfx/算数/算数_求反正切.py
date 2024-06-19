import math


def 算数_求反正切(值):
    """
    计算给定值的反正切值。

    参数:
    - 值 (float): 要计算反正切值的数值。

    # 示例用法
    value = 1
    atan_value = 算数_求反正切(value)
    print(f"{value}的反正切值为: {atan_value} 度")

    返回:
    - 角度 (float): 给定值的反正切值，返回的角度单位为度。
    """
    # 计算反正切值，结果为弧度
    弧度 = math.atan(值)

    # 将弧度转换为角度
    角度 = math.degrees(弧度)

    return 角度



