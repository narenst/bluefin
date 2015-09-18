#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '1.7'

__build__ = ''

setup(name='bluefin',
      version=__version__ + __build__,
      description='Meetup assitant application',
      author='Naren',
      author_email='narenst@gmail.com',
      url='http://narenst.github.io',
      packages=find_packages(exclude=['*.tests']),
      install_requires=[
          'flask',
          'rethinkdb'
      ],
      entry_points={
          'console_scripts': [
              'development = bluefin.development:main',
          ],
      },
      )
