import imaplib


def 邮件IMAP_连接服务器(服务器地址):
    """
    连接到IMAP服务器。

    参数:
        服务器地址 (str): IMAP服务器地址。

    返回:
        IMAP4_SSL 或 None: 成功返回 连接对象，失败返回 None。
    """
    try:
        邮箱 = imaplib.IMAP4_SSL(服务器地址)
        return 邮箱
    except Exception:
        return None