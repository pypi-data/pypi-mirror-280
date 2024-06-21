from setuptools import setup

name = 'shellium'
version = '1.0'
author = 'GooseG4G'
email = 'danilnegusev@inbox.ru'
desc = 'The package provides a wrapper for working with chrome driver.'
url = 'https://github.com/GooseG4G/shellium'
packages = ['shellium']
requires = []

setup(
    name=name,
    version=version,
    author=author,
    author_email=email,
    description=desc,
    url=url,
    packages=packages,
    install_requires=requires
)
