# setup.py

from setuptools import setup, find_packages

setup(
    name='process_file',
    version='0.1.0',
    description='Biblioteca que processa configurações locais',
    author='Rafael Gomes de Oliveira',
    author_email='rafaelprotest4@gmail.com',
    packages=find_packages(),
    install_requires=[
        'psutil~=6.0.0'
    ],
)
