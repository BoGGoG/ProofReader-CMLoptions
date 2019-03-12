#!/bin/env python3

#######################################################################
# Copyright (C) 2019 David Palao
#
# This file is part of ProofReader.
#
#  ProofReader is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ProofReader is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ProofReader.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################

from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="ProofReader",
    version="0.1.2",
    description="A proofreader of English texts",
    long_description=long_description,
    author="David Palao",
    author_email="palao@csc.uni-frankfurt.de",
    url="https://bitbucket.org/palao-csc/proofreader/",
    packages=find_packages(),
    entry_points={
        'console_scripts': ["proofread = proofreader.proofread:main"],
    },
    classifiers=[
        "Environment :: Console",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
)

