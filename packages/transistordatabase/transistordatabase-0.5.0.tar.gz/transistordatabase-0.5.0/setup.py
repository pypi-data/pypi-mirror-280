#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

# with open('requirements.txt', 'r') as f:
#    requirements = f.read().splitlines()

setup_requirements = ['setuptools_scm']

test_requirements = ['mongomock']

setup(
    author="LEA - Uni Paderborn",
    author_email='tdb@lea.upb.de',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Environment :: MacOS X'
    ],
    description="Transistor Database",
    install_requires=[
        'numpy>=1.19.5',
        'persistent>=4.6.4',
        'scipy>=1.6.0',
        'setuptools>=49.2.1',
        'pymongo>=3.11.3',
        'matplotlib>=3.3.4',
        'Jinja2 >= 3.0.1',
        'packaging>=20.9',
        'Pillow>=8.3.1',
        'pytest>=6.2.4',
        'PyQt5',
        'PyQtWebEngine',
        'mongomock',
        'requests',
        'deepdiff'],
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='Transistordatabase',
    name='transistordatabase',
    packages=find_packages(include=['transistordatabase', 'transistordatabase.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    extras_require={},
    url='https://github.com/upb-lea/transistordatabase',
    project_urls={
        "Documentation": "https://upb-lea.github.io/transistordatabase/main/transistordatabase.html",
        "Source Code": "https://github.com/upb-lea/transistordatabase",
    },
    version='0.5.0',
    zip_safe=False,
    data_files=[('', ['CHANGELOG.md'])]
)
