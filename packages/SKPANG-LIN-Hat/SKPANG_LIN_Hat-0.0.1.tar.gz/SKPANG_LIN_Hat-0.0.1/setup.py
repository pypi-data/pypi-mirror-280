from setuptools import setup, find_packages
from os import path
working_directory = path.abspath(path.dirname(__file__))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SKPANG_LIN_Hat', # name of packe which will be package dir below project
    version='0.0.1',
    #url='https://joseph.szlavik@scm.mclaren.com/Tools/Infotainment/Iceberg-Services/Prism/LIN_Library',
    author='Joseph Szlavik',
    author_email='joseph.szlavik@mclaren.com',
    description='LIN Communications Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(), #auto_discover packages
    install_requires=[],
)
url='https://joseph.szlavik@scm.mclaren.com/Tools/Infotainment/Iceberg-Services/Prism/LIN_Library'