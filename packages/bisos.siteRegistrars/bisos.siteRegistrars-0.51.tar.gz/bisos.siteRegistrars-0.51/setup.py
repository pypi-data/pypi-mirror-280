#!/usr/bin/env python

import setuptools
#import sys
import re

def readme():
    with open('./README.org') as file:
        while line := file.readline():
            if match := re.search(r'^#\+title: (.*)',  line.rstrip()):
                return match.group(1)
            return "MISSING TITLE in ./README.org"

def longDescription():
    try:
        import pypandoc
    except ImportError:
        result = "warning: pypandoc module not found, could not convert to RST"
        return result
    return pypandoc.convert_file('README.org', 'rst')

####+BEGIN: b:py3:pypi/nextVersion :increment 0.01

def pkgVersion(): return '0.51'
####+END:

#__version__ = get_version('unisos/icm/__init__.py')
__version__ = '0.4'


####+BEGIN: b:py3:pypi/requires :extras ("bisos.transit")

requires = [
"blee",
"blee.csPlayer",
"blee.icmPlayer",
"bisos",
"bisos.b",
"bisos.banna",
"bisos.bpo",
"bisos.cntnr",
"bisos.common",
"bisos.currents",
"bisos.debian",
"bisos.marmee",
"bisos.regfps",
"bisos.usgAcct",
"bisos.transit",
]
####+END:

####+BEGIN: b:py3:pypi/scripts :comment ""

scripts = [
'./bin/siteRegistrarsDaemonSysd.cs',
'./bin/siteRegistrarsRuns.cs',
'./bin/svcInvSiteRegBox.cs',
'./bin/svcInvSiteRegContainer.cs',
'./bin/svcPerfSiteRegistrars.cs',
'./bin/svcSiteRegBox.cs',
'./bin/svcSiteRegContainer.cs',
'./bin/svcSiteRegistrars.cs',
'./bin/svcSiteRegNets.cs',
]
####+END:



oldrequires = [
    'bisos.currents',
]

oldscripts = [

    "bin/svcSiteRegBox.cs",
    "bin/svcInvSiteRegBox.cs",
    "bin/svcSiteRegNets.cs",
    "bin/svcSiteRegContainer.cs",
    "bin/svcSiteRegistrars.cs",
    "bin/svcPerfSiteRegistrars.cs",
    "bin/svcInvSiteRegContainer.cs",
    "bin/siteRegistrarsDaemonSysd.cs",
    "bin/siteRegistrarsRuns.cs",
]

#
# Data files are specified in ./MANIFEST.in as:
# recursive-include unisos/marme-base *
# recursive-include unisos/marme-config *
#
    
data_files = [
]

setuptools.setup(
    name='bisos.siteRegistrars',
    # version=__version__,
    version=pkgVersion(),
    namespace_packages=['bisos'],
    packages=setuptools.find_packages(),
    scripts=scripts,
    #data_files=data_files,
    include_package_data=True,
    zip_safe=False,
    author='Mohsen Banan',
    author_email='libre@mohsen.1.banan.byname.net',
    maintainer='Mohsen Banan',
    maintainer_email='libre@mohsen.1.banan.byname.net',
    url='http://www.by-star.net/PLPC/180047',
    license='AGPL',
    description=readme(),
    long_description=longDescription(),
    download_url='http://www.by-star.net/PLPC/180047',
    install_requires=requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )

