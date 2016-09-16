#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='indicolite',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Browse Indico from the command line",
    long_description="Download all material from a list of categories.",
    scripts=['indicolite'],
    data_files=[('share/man/man1', ['indicolite.1'])],
)
