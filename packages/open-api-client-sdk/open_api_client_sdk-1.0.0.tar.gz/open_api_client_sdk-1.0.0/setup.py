# -*- coding:utf-8 -*-
"""
 @author: huang
 @date: 2024-05-21
 @File: setup.py
 @Description: 
"""

from setuptools import setup, find_packages

setup(
    name='open_api_client_sdk',
    version='1.0.0',
    description='Python SDK for Open API platform',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='elasticcode',
    author_email='hzreal0823@outlook.com',
    url='https://github.com/elasticcode/open-api-client-sdk-python',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)