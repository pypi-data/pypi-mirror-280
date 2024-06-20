from setuptools import setup, find_packages

setup(
    name='pychanneldock',
    version='0.3.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    descrtiption='A Python wrapper for the Channeldock API',
    author='Hango Bogdan')
