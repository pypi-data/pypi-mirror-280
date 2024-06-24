from setuptools import setup, find_packages

setup(
    name='ossconer',
    version='0.0.4',
    description='Python交互OSS，更方便地使用一些常用功能',
    author='WangTuo',
    author_email='markadc@126.com',
    packages=find_packages(),
    license='MIT',
    zip_safe=False,
    install_requires=['oss2'],
    keywords=['Python', 'OSS'],
)

"""
    2024-6-21  如果OSS路径已存在，可以选择返回地址或者False
    2024-6-24  大更新，优化架构、参数、返回值等
"""