#!/usr/bin/python
#-*- coding:utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="hanryi-utils", # pip项目发布的名称
    version="0.0.4", 
    author="Hanryi", 
    author_email="hanry.rui@gmail.com",
    description="Hanryi's private utils.", 
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url="https://github.com/Hanryi/hanryi-utils", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)