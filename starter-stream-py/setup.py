# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='twitter_stream_py_poc',
    version='0.1.0',
    description='POC for realtime sentiment analysis of Twitter streams',
    long_description=readme,
    author='Denise Gosnell',
    author_email='denise.gosnell@datastax.com',
    url='https://github.com/ucsd-capstone-datastax/prototypes',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
