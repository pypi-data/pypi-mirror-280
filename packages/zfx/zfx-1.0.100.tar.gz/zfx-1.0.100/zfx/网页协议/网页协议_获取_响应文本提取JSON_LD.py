import extruct
from w3lib.html import get_base_url


def 网页协议_获取_响应文本提取JSON_LD(响应对象):
    """
    提取 HTTP 响应对象中的 json-LD 数据，并返回一个包含所有 json-LD 数据的列表。

    参数:
    - 响应对象: 服务器响应对象。

    返回值:
    - 包含所有 json-LD 数据的列表。如果提取过程中出现异常，则返回空列表。
    """
    try:
        # 获取 HTML 内容和基准 URL
        内容 = 响应对象.text
        基准URL = get_base_url(响应对象.text, 响应对象.url)

        # 使用 extruct 提取嵌入的数据
        data = extruct.extract(内容, base_url=基准URL)

        # 提取所有的 json-LD 数据并添加到列表中
        json列表 = data.get('json-ld', [])
        return json列表
    except Exception:
        return []