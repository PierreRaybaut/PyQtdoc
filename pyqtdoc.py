# postinstall script for PyQtdoc
"""Register qch files with QtAssistant"""

from __future__ import print_function

import os
import sys
import os.path as osp
import subprocess
import argparse


def register(rollback=False):
    parser = argparse.ArgumentParser(description="Register .qch files to Qt Assistant")
    parser.add_argument("action", choices=["register", "unregister"])
    args = parser.parse_args()
    rollback = args.action == "unregister"
    prefix = "Unr" if rollback else "R"
    print(prefix + "egistering .qch files in Qt Assistant:")
    exe_dir = osp.join(sys.prefix, "Lib", "site-packages", "pyqt5_tools", "Qt", "bin")
    command = [
        osp.join(exe_dir, "assistant.exe"),
        "-quiet",
        "-%segister" % prefix.lower(),
    ]
    qch_dir = osp.join(sys.prefix, "Lib", "site-packages", "PyQtdoc")
    for name in os.listdir(qch_dir):
        if osp.splitext(name)[1] == ".qch":
            print("    " + name)
            cmd = command + [osp.abspath(osp.join(qch_dir, name))]
            proc = subprocess.Popen(" ".join(cmd), shell=True)
            proc.wait()
    print("Done.")


if __name__ == "__main__":
    register()
