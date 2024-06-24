import os


def 目录_取桌面目录():
    """
    获取当前用户的桌面目录路径。

    返回:
        str: 当前用户的桌面目录路径。如果获取失败或异常则返回 None。

    示例:
        桌面目录 = 目录_取桌面目录()
        if 桌面目录 is not None:
            print("桌面目录路径:", 桌面目录)
        else:
            print("获取桌面目录失败")
    """
    try:
        if os.name == 'nt':  # Windows
            桌面目录 = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        else:  # macOS 和 Linux
            桌面目录 = os.path.join(os.path.expanduser('~'), 'Desktop')
        return 桌面目录 if os.path.exists(桌面目录) else None
    except Exception:
        return None
