#!/usr/bin/python3
from setuptools import setup

setup(
   name='RESTTestPY',
   version='1.0',
   description='Test Restful web APIs',
   author='Valentin Kormanov',
   author_email='guve4e@gmail.com',
   packages=['RESTTestPY'],
   install_requires=['tqdm'], #external packages as dependencies
)