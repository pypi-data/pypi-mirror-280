from setuptools import setup, find_packages

setup(
    name='pychanneldock',
    version='0.3.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
    ],
    descrtiption='A Python wrapper for the Channeldock API',
    author='Hango Bogdan')
