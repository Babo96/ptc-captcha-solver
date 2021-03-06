import os
from io import open
from setuptools import setup

DIST_NAME = 'Pikapy'
VERSION = 'v0.3'
AUTHOR = 'skvvv'
EMAIL = 'skvvv.og@gmail.com'
GITHUB_USER = 'skvvv'
GITHUB_URL = 'https://github.com/{GITHUB_USER}/{DIST_NAME}'.format(**locals())

# Get the long description from the README file
setup_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(setup_dir, 'README.md'), encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name=DIST_NAME,
    packages=['pikapy'],
    version=VERSION,
    description='Pokemon Go Bulk Account Creator.',
    author=AUTHOR,
    author_email=EMAIL,
    url=GITHUB_URL,
    license='GPL v3',
    download_url='{GITHUB_URL}/tarball/{VERSION}'.format(**locals()),
    keywords='',
    install_requires=[
        'requests[security]==2.10.0',
        'six==1.10.0',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    entry_points={
        'console_scripts': [
            'pikapy = pikapy.console:entry',
        ],
    }
)
