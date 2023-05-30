# -*- coding: utf-8 -*-

# Third
from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Api Python Flask'
__long_description__ = 'This is an API to Flask Api Users'

__author__ = 'Danillo Silva'
__author_email__ = 'danlloaugustobsilva@hotmail.com'


testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='api',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/danbsilva/',
    keywords='API, Flask',
    include_package_data=True,
    zip_safe=False,
)