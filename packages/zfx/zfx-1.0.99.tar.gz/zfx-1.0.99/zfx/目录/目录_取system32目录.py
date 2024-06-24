import os


def 目录_取system32目录():
    """
    获取系统中 System32 目录的路径。

    返回:
        str: System32 目录的路径，如果操作失败则返回空字符串
    """
    try:
        # 使用 os.environ 获取环境变量中的 SystemRoot
        system_root = os.environ.get('SystemRoot', 'C:\\Windows')
        # 构造 System32 目录的完整路径
        system32_path = os.path.join(system_root, 'System32')

        # 检查路径是否存在，并且确保是一个目录
        if os.path.exists(system32_path) and os.path.isdir(system32_path):
            return system32_path
        else:
            return ""
    except Exception as e:
        return ""
