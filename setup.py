#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
	name = "demo",
	version = "0.1",
	url = 'https://github.com/snowroll/python-sdk.git',
	long_description = open('README.md').read(),
	packages = find_packages(),
)

'''
name 包的名字
version 依赖关系很重要
packages 需要包含的子包列表，用find_packages()查找
url：包的链接，通常为 Github 上的链接，或者是 readthedocs 链接
setup_requires：指定依赖项
test_suite：测试时运行的工具
'''