#!/usr/bin/env python

import os

from setuptools import setup

def long_description():
    base_dir = os.path.dirname(__file__)
    readme_f = open(os.path.join(base_dir, 'README.md'))
    try:
        readme = readme_f.read()
    finally:
        readme_f.close()
    return readme

setup(
    name='password-permute',
    version='0.2',
    description="Rearrange generated passwords so they're easier to type "
                "on a mobile device",
    long_description=long_description(),
    author='Alex Willmer',
    author_email='alex@moreati.org.uk',
    py_modules=['password_permute'],
    url='https://github.com/moreati/password-permute',
    classifiers = [
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security',
        ],
    entry_points={
        'console_scripts': [
            'password-permute = password_permute:main',
            ],
        },
    )
