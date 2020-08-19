# -*- coding: utf-8 -*-
"""PyQt doc"""

import setuptools  # analysis:ignore
from distutils.core import setup
import os
import os.path as osp

assert os.name == "nt"  # For Windows platforms only!


def get_data_files(dirname):
    """Return data files in directory *dirname*"""
    flist = []
    for dirpath, _dirnames, filenames in os.walk(dirname):
        for fname in filenames:
            flist.append(osp.join(dirpath, fname))
    return flist


NAME = "PyQtdoc"
VERSION = "5.15.0"

setup(
    name=NAME,
    version=VERSION,
    description="%s installs Qt documentation for PyQt" % NAME,
    long_description="""%s installs Qt official documentation 
(.ch files, i.e. Qt assistant format) in PyQt directory.

%s version is indexed to Qt version.

%s is part of the WinPython distribution project.

Important note
--------------

    Since Qt5, ``QtAssistant`` cannot register documentation automatically. You must run the ``scripts\pyqtdoc.py`` script (with option `--register`) or register them manually.
"""
    % (NAME, NAME, NAME),
    data_files=[(osp.join("Lib", "site-packages", NAME), get_data_files("qch"))],
    requires=["PyQt5", "pyqt5_tools"],
    author="Pierre Raybaut",
    author_email="pierre.raybaut@gmail.com",
    url="https://github.com/PierreRaybaut/PyQtdoc",
    classifiers=["Operating System :: Microsoft :: Windows"],
    scripts=["%s.py" % NAME.lower()],
)
