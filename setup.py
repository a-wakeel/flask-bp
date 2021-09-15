"""
This file based on the example from the PyPA sample project, whose copyright is
included below:
Copyright (c) 2016 The Python Packaging Authority (PyPA)
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""
from setuptools import setup, find_packages
from codecs import open
from os import path
import re
import sys

here = path.abspath(path.dirname(__file__))

# allow python 3 only
if sys.version_info[0] != 3:
    sys.exit('Sorry, only python 3.x supported')

# get long description from readme file, you can use any other
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Version snippet from the following URL:
# https://github.com/pypa/python-packaging-user-guide/blob/master/source/single_source_version.rst
#
# The Python Packaging User Guide is licensed under a Creative Commons
# Attribution-ShareAlike license: http://creativecommons.org/licenses/by-sa/3.0
#


def read(*names):
    with open(path.join(here, *names), encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    """Method to find the version string."""
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='flask_bp',
    version=find_version('src/flask_bp', '__init__.py'),
    url='',
    license='MIT',
    author='a-wakeel',
    author_email='',
    description='Boilerplate for flask based apps',
    long_description=long_description,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    entry_points={}
)
