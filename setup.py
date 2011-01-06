#!/usr/bin/env python

from distutils.core import setup

setup(name='ConfigObj-Qt',
		version='0.1',
		description='Save and load ConfigObj configuration data using PyQt. This enables configuration to be stored in a way that is appropriate for the platform where the application is running.',
		author='Stefan Parviainen',
		author_email='pafcu@iki.fi',
		url='https://github.com/pafcu/ConfigObj-Qt',
		classifiers=('Development Status :: 4 - Beta',
			'License :: OSI Approved :: ISC License (ISCL)',
			'Intended Audience :: Developers',
			'Topic :: Software Development :: Libraries :: Python Modules'
			),
		platforms=('Any'),
		requires=('PyQt', 'ConfigObj'),
		py_modules=['configobj_qt']
		)
