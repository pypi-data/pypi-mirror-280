from setuptools import setup, find_packages
import codecs
import os 


VERSION = '0.0.1'
DESCRIPTION = 'A library for lexing and parsing'
LONG_DESCRIPTION = """
    a python lib for lexing and parsing your code 
"""
setup(
    name="ParserLexing",
    version=VERSION,
    author="Amir Sabri",
    author_email="amirsbry1942@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
)