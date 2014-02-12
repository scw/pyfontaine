#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# fontaine.py
#
# Copyright (c) 2013,
# Виталий Волков <hash.3g@gmail.com>
# Dave Crossland <dave@understandinglimited.com>
#
# Released under the GNU General Public License version 3 or later.
# See accompanying LICENSE.txt file for details.

from setuptools import setup

with open("README.md", 'r') as readme_file:
    readme = readme_file.read()

setup(name='fontaine',
      version='1.1.1',
      description='Fontaine font tool',
      license="GNU GPLv3",
      long_description=readme,
      author='Dave Crossland, Виталий Волков',
      author_email='dave@lab6.com',
      url='https://github.com/davelab6/pyfontaine',
      # more examples here http://docs.python.org/distutils/examples.html#pure-python-distribution-by-package
      packages=['fontaine', 'fontaine.charmaps', 'fontaine.structures', 'fontaine.ext'],
      install_requires=[
          'fonttools',
          'lxml',
          'matplotlib',
          'requests'
      ],
      package_data={
          'fontaine': [
              'charmaps/names.db/*.*',
              'charmaps/fontconfig/fc-lang/*.orth'
          ]
      },
      scripts=['bin/simpleHilbertCurve',
               'bin/pyfontaine'])
