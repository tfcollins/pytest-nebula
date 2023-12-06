#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-nebula',
    version='0.1.0',
    author='Travis Collins',
    author_email='travis.collins@analog.com',
    maintainer='Travis Collins',
    maintainer_email='travis.collins@analog.com',
    license='Apache Software License 2.0',
    url='https://github.com/tfcollins/pytest-nebula',
    description='pytest plugin for nebula dev kit manager',
    long_description=read('README.rst'),
    packages=["pytest_nebula"],
    # package_data={"pytest_libiio": ["resources/*"]},
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0','nebula'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points={
        'pytest11': [
            'nebula = pytest_nebula.plugin',
        ],
    },
)
