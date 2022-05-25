#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "1.0"

setup(name='TS_Evolutionary_Prototyping',
      version = __version__,
      description='A library to find the prototype in large sets of series',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Pablo Leon-Alcaide',
      author_email='Luis.Rodriguez@uclm.es',
      url="https://github.com/lrbenitez/TS_Evolutionary_Prototyping",
      py_modules = ['TS_Evolutionary_Prototyping'],
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Beta',

          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',

          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 0.3.1',
          'Topic :: Scientific/Engineering',
      ],
      keywords='lib Time Series prototyping',

      packages=find_packages(exclude=["docs"]),

      install_requires = ['numpy','scipy',
                          'sklearn',
                          'numba',
                          'pandas', 
                          'wheel',
                          'matplotlib',
                          'deap'],

      extras_require = {
          'doc': ["sphinx", "numpydoc"]
          }
)
