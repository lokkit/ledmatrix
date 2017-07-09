#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
    'Adafruit-LED-Backpack==1.8.1',
    'Pillow==2.6.1'
]

setup(
    name='ledmatrix',
    version='0.1.0',
    description="Tool to display stuff on 8x8 matrix for lokkit demonstrator",
    long_description=readme + '\n\n',
    author="Andreas Schmid",
    author_email='ikeark@gmail.com',
    url='https://github.com/kraeki/ledmatrix',
    packages=find_packages(include=['ledmatrix']),
    entry_points={
        'console_scripts': [
            'ledmatrix=ledmatrix.cli:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='ledmatrix',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
)
