# -*- coding: utf-8 -*-
"""PyQt doc"""

from distutils.core import setup
import os
import os.path as osp

assert os.name == 'nt'  # For Windows platforms only!

def get_data_files(dirname):
    """Return data files in directory *dirname*"""
    flist = []
    for dirpath, _dirnames, filenames in os.walk(dirname):
        for fname in filenames:
            flist.append(osp.join(dirpath, fname))
    return flist

NAME = 'PyQtdoc'
VERSION = '5.5.1'

setup(name=NAME, version=VERSION,
      description='%s installs Qt documentation for PyQt' % NAME,
      long_description="""%s installs Qt official documentation 
(.ch files, i.e. Qt assitant format) in PyQt directory.

%s version is indexed to NumPy version.

%s is part of the WinPython distribution project.
""" % (NAME, NAME, NAME),
      data_files=[(r'Lib\site-packages\PyQt%s\doc\qch' % VERSION.split('.')[0],
                   get_data_files('qch'))],
      requires=["PyQt%s" % VERSION.split('.')[0],],
      author = "Pierre Raybaut",
      author_email = 'pierre.raybaut@gmail.com',
      url = 'https://github.com/PierreRaybaut/PyQtdoc',
      classifiers=['Operating System :: Microsoft :: Windows'],
	  scripts=['%s_win_post_install.py' % NAME],
	  options={"bdist_wininst":
               {"install_script": "%s_win_post_install.py" % NAME,
                "title": "%s %s" % (NAME, VERSION),
                "user_access_control": "auto"},
               "bdist_msi":
               {"install_script": "%s_win_post_install.py" % NAME}},
			   )
