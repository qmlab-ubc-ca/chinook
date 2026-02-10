# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 11:18:28 2018

@author: rday
"""

from setuptools import setup, find_packages

def readme():
    with open("README.rst", encoding="utf-8") as f:
        return f.read()
    
setup(name= 'chinook',
      version = '1.1.4.dev0',
      author = 'Ryan P. Day', 
      author_email = 'ryanday7@gmail.com',
      description = 'Tools for tight-binding and simulation of ARPES',
      long_description=readme(),
      url = 'https://github.com/qmlab-ubc-ca/chinook',
      classifiers =[
		'Development Status :: 4 - Beta',              
		'License :: OSI Approved :: MIT License',              	
		'Programming Language :: Python :: 3 :: Only',             
        	'Topic :: Scientific/Engineering :: Physics',
          'Operating System :: OS Independent'
	      ],
      license= 'MIT',
      packages= find_packages(),
      install_requires=['numpy','matplotlib','scipy'],
      include_package_data=True,
      python_requires=">=3.9",
      package_data = {'chinook': ['*.txt']}
      )
