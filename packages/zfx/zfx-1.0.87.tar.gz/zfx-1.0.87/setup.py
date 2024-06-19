from setuptools import setup, find_packages

setup(
    name='zfx',
    version='1.0.87',
    packages=find_packages(),
    # 不包含其他文件
    include_package_data=False,
    # 作者信息等
    author='zengfengxiang',
    author_email='424491679@qq.com',
    description='中国人自己的模块！ZFX是一个多功能的Python工具包，提供了各种实用工具和功能，包括网络请求、剪贴板操作、系统监控、网页自动化、系统操作、文本处理、文件操作等。我们主打技术分享和交流，致力于为Python开发者提供一个共享知识、解决问题的平台。无论是日常办公还是自动化脚本，ZFX都能为您提供便捷的解决方案，让您的编程体验更加愉快！',
    # 项目主页
    url='',
    # 依赖列表
    install_requires=[
        'requests',
        'pyperclip',
        "pystray",
        "psutil",
        "selenium",
        "requests",
        "mysql.connector",
        "pyinstaller",
        "openpyxl",
        "jsonpath",
        # 添加其他依赖库
    ],
)


