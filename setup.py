#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
'pandas',
'xlrd==1.2.0',
'stats-arrays',
'jupyter'
]

setup_requirements = [ ]

package_input_data = {'swolfpy_inputdata.Data':['*.csv'],
                      'swolfpy_inputdata.Data.LCIA_Methods':['*.csv']}
                                                                

test_requirements = [ ]

files = None


setup(
    author="Mojtaba Sardarmehni",
    author_email='msardar2@ncsu.edu',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Natural Language :: English',
    ],
    description="Input data for swolfpy's life-cycle process models (swolfpy_inputdata)",
    install_requires=requirements,
    license="GNU GENERAL PUBLIC LICENSE V2",
    long_description=readme + '\n\n' + history,
    long_description_content_type= 'text/x-rst',
    include_package_data=True,
    keywords='swolfpy_inputdata',
    name='swolfpy_inputdata',
    packages=find_packages(include=['swolfpy_inputdata', 'swolfpy_inputdata.*']),
    setup_requires=setup_requirements,
    package_data=package_input_data,
    data_files = files,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://bitbucket.org/msm_sardar/swolfpy-inputdata',
    version='0.1.9',
    zip_safe=False,
)
