#!/bin/python3
# coding: utf-8
"""chios setup file."""

# To use a consistent encoding
from codecs import open
from os import path

from setuptools import find_packages, setup

from chios import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='chios',
    version=__version__,
    description='A collection of Sphinx extensions.',
    long_description=long_description,
    url='https://github.com/kallimachos/chios',
    author='Brian moss',
    author_email='kallimachos@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Documentation :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='sphinx documentation extension bold italic remote code',
    packages=find_packages(exclude=['tests']),
    package_data={
        'chios.bolditalic': ['bolditalic.css']
    },
    install_requires=['docutils', 'requests', 'sphinx'],
)
