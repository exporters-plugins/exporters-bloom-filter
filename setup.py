# flake8: noqa
from setuptools import setup, find_packages

setup(
    name = 'exporters_bloom_filter',
    version = '0.1.5',
    author = 'Bernardo Botella',
    author_email = 'contacto@bernardobotella.com',
    packages = find_packages(exclude=['tests']),
    install_requires = ['exporters', 'pybloom'],
)
