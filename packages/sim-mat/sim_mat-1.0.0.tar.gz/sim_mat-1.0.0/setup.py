# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:47:50 2024

@author: EL221XK
"""

# setup.py

from setuptools import setup, find_packages

setup(
    name='sim_mat',
    version='1.0.0',
    packages=find_packages(),
    author='Afreen Aman',
    author_email='afreenaman90@gmail.com',
    description='A brief description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AfreenAman/Mathfunc',
    license='Apache',
    install_requires=[
        # List of dependencies if any
    ],
)
