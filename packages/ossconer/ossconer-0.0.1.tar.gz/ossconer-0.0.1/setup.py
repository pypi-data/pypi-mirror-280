from setuptools import setup, find_packages

setup(
    name='ossconer',
    version='0.0.1',
    description='Python交互OSS，更方便地使用一些常用功能',
    author='WangTuo',
    author_email='markadc@126.com',
    packages=find_packages(),
    license='MIT',
    zip_safe=False,
    install_requires=['oss2'],
    keywords=['Python', 'OSS'],
)
