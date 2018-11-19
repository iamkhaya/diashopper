#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open('version') as fd:
    version = fd.read().strip()

with open('requirements.txt') as fd:
    requirements = [
        dependency.strip() for dependency in
        [
            (dep.split('#', 1)[0]).strip() for dep in fd
        ]
        if dependency
    ]

setup_args = {
    'name': 'diashopper',
    'version': version,
    'description': 'diashopper',
    'author': 'Finance Team',
    'author_email': 'khayelihle.tshuma@gmail.com',
    'url': 'https://github.com/iamkhaya',
    'packages': find_packages(exclude=['tests']),
    'install_requires': requirements,
    'classifiers': [
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    'entry_points': {
        'console_scripts': [
        ],
    }
}

setup(**setup_args)
