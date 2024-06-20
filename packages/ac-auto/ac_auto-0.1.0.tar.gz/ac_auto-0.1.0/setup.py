from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='ac_auto',  # 包名
    version='0.1.0',  # 版本号
    description='文本多模匹配AC自动机的Python实现',
    long_description=long_description,
    author='ray.ping',
    author_email='342099577@qq.com',
    url='',
    install_requires=[
        'jieba >= 0.42.1'
    ],  # 依赖包会同时被安装
    license='MIT',
    packages=find_packages()
)
