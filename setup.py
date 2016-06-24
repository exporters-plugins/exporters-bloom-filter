# flake8: noqa
from setuptools import setup, find_packages

setup(
    name = 'exporters bloom filter',
    version = '0.1.2',
    author = 'Bernardo Botella',
    author_email = 'contacto@bernardobotella.com',
    packages = find_packages(exclude=['tests']),
    install_requires = ['exporters', 'pybloom'],
)
