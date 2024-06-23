# setup.py

from setuptools import setup, find_packages

setup(
    name='banco_dados',
    version='0.1.0',
    description='Biblioteca que executa ações no banco de dados',
    author='Rafael Gomes de Oliveira',
    author_email='rafaelprotest4@gmail.com',
    packages=find_packages(),
    install_requires=[
        'mysql-connector-python',
        'python-dotenv',
    ],
)
