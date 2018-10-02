"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/rkoeninger/tictactoe
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tictactoe',
    version='0.0.1',
    description='Classic Tic-Tac-Toe game',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rkoeninger/tictactoe',
    author='Robert Koeninger',
    author_email='rkoeninger@att.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='game ai tictactoe',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    entry_points={
        'console_scripts': [
            'tictactoe=tictactoe:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/rkoeninger/tictactoe/issues',
        'Source': 'https://github.com/rkoeninger/tictactoe/',
    },
)
