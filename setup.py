# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in namlifa_portal/__init__.py
from namlifa_portal import __version__ as version

setup(
	name='namlifa_portal',
	version=version,
	description='Namlifa Portal by ERP-X',
	author='ERP-X',
	author_email='dev.erpx@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
