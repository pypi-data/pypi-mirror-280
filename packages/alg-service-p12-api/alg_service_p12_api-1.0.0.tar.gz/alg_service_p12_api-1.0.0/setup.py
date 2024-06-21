#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
__author__ = "L.K"

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("3rd.list", "r") as fh:
    requirements = fh.readlines()

pks = find_packages()  # .append('agent.py')
print(pks)

setup(name='alg-service-p12-api',
      version='1.0.0',  #
      description='alg service grpc api (for python3.7 )',  #
      author='L.K',  #
      author_email='L.K@idontwant.com',  #
      url='',  #
      packages=pks,  # Python导入包的列表，我们使用find_packages() 来自动收集
      long_description=long_description,  #
      long_description_content_type="text/markdown",  #

      classifiers=[
          "Programming Language :: Python :: 3",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Operating System :: POSIX :: Linux"],

      python_requires='>=3.12',  # Python 的版本约束
      install_requires=requirements
      )
