#! /usr/bin/env python
from distutils.core import setup
from setuptools import find_packages
import sys

# python2 and python3 support
try:
    reload
except NameError:
    # py3k has unicode by default
    pass
else:
    reload(sys).setdefaultencoding('utf-8')


setup(
    name='django-tabbed-admin-u',
    version='1.0.4',
    author='intp1',
    author_email='intp1@protonmail.com',
    description="Patched with 'ugettext/gettext' support for django-tabbed-admin",
    long_description=open('README.rst').read(),
    url='http://www.revsquare.com',
    license='BSD License',
    platforms=['OS Independent'],
    packages=find_packages("./tabbed_admin", include=['*.py','*.txt','static.*','templates.*','templatetags.*']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)
