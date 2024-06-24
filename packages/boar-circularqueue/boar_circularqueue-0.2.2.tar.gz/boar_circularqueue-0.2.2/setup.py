#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Dexter Chan",
    author_email='dexterchan@example.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.11',
    ],
    description="A circular queue supports simple demo",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='boar_circularqueue',
    name='boar_circularqueue',
    packages=find_packages(include=['boar_circularqueue', 'boar_circularqueue.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dexterchan/circularqueue',
    version='0.2.2',
    zip_safe=False,
)
