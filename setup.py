#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# =============================================================================
# File      : setup.py -- Setup script for git2net
# Author    : Ingo Scholtes <ingo.scholtes@uni-wuerzburg.de>
# Time-stamp: <Tue 2022-01-04 17:05>
"""
Setup script for git2net.
"""
import sys
import os
from setuptools import setup, find_packages

about = {}
base_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(base_dir, 'git2net', '__about__.py'), 'rb') as f:
    exec(f.read(), about)

version = about['__version__']

# Minimum required python version
min_version = (3, 7)

# Check the python version. Pathpy requires Python 3.7+.
if sys.version_info[:2] < min_version:
    error = """
    git2net {} requires Python {} or later ({} detected).

    """.format(version,
               '.'.join(map(str, min_version)),
               '.'.join(map(str, sys.version_info[:2])))
    sys.exit(error)


# Initialize setup parameters
DISTNAME = 'git2net'

VERSION = version

PYTHON_REQUIRES = '>={}'.format('.'.join(map(str, min_version)))

DESCRIPTION = "git2net"

LONG_DESCRIPTION = """\
An Open Source Python package that facilitates the extraction of co-editing networks from git repositories.
"""

MAINTAINER = 'Christoph Gote'

MAINTAINER_EMAIL = 'cgote@ethz.ch'

URL = 'https://github.com/gotec/git2net'

LICENSE = 'AGPL-3.0+'

DOWNLOAD_URL = 'https://github.com/gotec/git2net'

PROJECT_URLS = {
    "Issue Tracker": "https://github.com/gotec/git2net/issues",
    "Documentation": "https://github.com/gotec/git2net/blob/master/TUTORIAL.ipynb",
    "Source Code": "https://github.com/gotec/git2net",
}

INSTALL_REQUIRES = [
    'setuptools>=42',
    'wheel',
    'pathpy'
]

PACKAGES = find_packages()

PLATFORMS = ['Linux', 'Mac OSX', 'Windows', 'Unix']

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Operating System :: OS Independent',
]


setup(
    name=DISTNAME,
    author=MAINTAINER,
    author_email=MAINTAINER_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license=LICENSE,
    url=URL,
    project_urls=PROJECT_URLS,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    install_requires=INSTALL_REQUIRES,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
    platforms=PLATFORMS,
    zip_safe=False,
    include_package_data=True,
    python_requires=PYTHON_REQUIRES
)

# =============================================================================
# eof
#
# Local Variables:
# mode: python
# mode: linum
# mode: auto-fill
# fill-column: 79
# End:
