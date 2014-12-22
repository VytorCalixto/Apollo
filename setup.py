#!/usr/bin/python
"""
setup for apollo
https://github.com/VytorCalixto/Apollo
"""

try:
    from setuptools import setup
except ImportError:
    from distutil.core import setup

setup(
    name="apollo",
    version="0.0.1",
    description="Manage your musical library",
    author="vytorcalixto",
    author_email="vytorcalixto@gmail.com",
    url="http://github.com/VytorCalixto/Apollo/",
    download_url="https://github.com/VytorCalixto/Apollo/tarball/master",
    install_requires=[
        'colorama>=0.3.2',    
    ],
    packages=['apollo_pkg'],
    entry_points=dict(console_scripts=['apollo = apollo_pkg:main.main']),
    license="MIT"
)
