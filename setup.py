#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as f:
	readme = f.read()

setup(
	name = "django-auth-oidc",
	version = "0.1.0",
	description = "OpenID Connect authentication support for Django",
	long_description = readme,
	author = "Linus Lewandowski",
	author_email = "linus@lew21.net",
	url = "https://github.com/LEW21/django-auth-oidc",
	keywords = "django,auth,oauth,openid,oidc,social,ldap",
	license = "LGPLv2+",

    install_requires = ["django>=1.10.0", "python-jose"],

	packages = ["django_auth_oidc"],
	package_data = {"": ["LICENSE"]},
	package_dir = {"django_auth_oidc": "django_auth_oidc"},
	zip_safe = True,
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: System Administrators',
		'Natural Language :: English',
		'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: System :: Systems Administration :: Authentication/Directory',
	]
)
