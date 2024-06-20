#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: Peoplees
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2024 Peoplees
"""

version = '1.0.0'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ExamLibrary',
    version=version,

    author='Peoplees',
    author_email='pulratv1@gmail.com',

    description=(
        u'Python module for writing scripts for project management platform '
        u'Club House (clubhouse.io API wrapper)'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Peopl3s/club-house-api',
    download_url='https://github.com/Peopl3s/club-house-api/archive/main.zip'.format(
        version
    ),

    license='Apache License, Version 2.0, see LICENSE file',

    packages=['ExamLibrary'],
    install_requires=['aiohttp', 'aiofiles'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)