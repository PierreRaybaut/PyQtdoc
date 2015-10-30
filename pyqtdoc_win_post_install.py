# postinstall script for PyQtdoc
"""Register qch files with QtAssistant"""

from __future__ import print_function

import os
import sys
import os.path as osp
import subprocess

def install():
    """Function executed when running the script with the -install switch"""
    pyqt_dir = osp.join(sys.prefix, 'Lib', 'site-packages', 'PyQt5')
    command = [osp.join(pyqt_dir, 'assistant.exe'), '-quiet', '-register']
    qch_dir = osp.join(pyqt_dir, 'doc', 'qch')
    for name in os.listdir(qch_dir):
        cmd = command + [osp.abspath(osp.join(qch_dir, name))]
        proc = subprocess.Popen(" ".join(cmd), shell=True)
        proc.wait()

def remove():
    """Function executed when running the script with the -remove switch"""
    pass

if __name__=='__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-install':
            try:
                install()
            except OSError:
                print("Failed to create Start Menu items.", file=sys.stderr)
        elif sys.argv[1] == '-remove':
            remove()
        else:
            print("Unknown command line option %s" % sys.argv[1],
                  file=sys.stderr)
    else:
        print("You need to pass either -install or -remove as options to "\
              "this script", file=sys.stderr)
