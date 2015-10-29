# -*- coding: utf-8 -*-
"""PyQt doc"""

from distutils.core import setup
import os
import os.path as osp

def get_data_files(dirname):
    """Return data files in directory *dirname*"""
    flist = []
    for dirpath, _dirnames, filenames in os.walk(dirname):
        for fname in filenames:
            flist.append(osp.join(dirpath, fname))
    return flist

PROJECT_NAME = 'PyQtdoc'
VERSION = '4.8.7'

setup(name=PROJECT_NAME, version=VERSION,
      description='%s installs Qt documentation for PyQt' % PROJECT_NAME,
      long_description="""%s installs Qt official documentation 
(.ch files, i.e. Qt assitant format) in PyQt directory.

%s version is indexed to NumPy version.

%s is part of the WinPython distribution project.
""" % (PROJECT_NAME, PROJECT_NAME, PROJECT_NAME),
      data_files=[(r'Lib\site-packages\PyQt%s\doc\qch' % VERSION.split('.')[0],
                   get_data_files('qch'))],
      requires=["PyQt%s" % VERSION.split('.')[0],],
      author = "Pierre Raybaut",
      author_email = 'pierre.raybaut@gmail.com',
      url = 'http://code.google.com/p/winpython/',
      classifiers=['Operating System :: Microsoft :: Windows'])
