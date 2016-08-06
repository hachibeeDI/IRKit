#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

install_requires = open('requirements.txt').read().split('\n')
readme_content = open('README.md').read()

from shutil import copyfile
copyfile('./main.py', './bin/irkit')


setup(
    name='irkit',
    version='0.0.4',
    description='Command line toolkit IRKIt HTTP api',
    long_description=readme_content,
    author='OGURA_Daiki',
    author_email='',
    license='MIT',
    keywords=['irkit', 'smart home'],
    url='https://github.com/hachibeeDI/IRKit',
    packages=find_packages(),
    scripts=['bin/irkit'],
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
