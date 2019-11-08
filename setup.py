from distutils.core import setup
import py2exe
import sys
import os

sys.argv.append('py2exe')
Mydata_files = [('.', ['builtins.txt', 'fndata.txt'])]
setup(
    data_files=Mydata_files,
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    console=[{'script': "main.py"}, {'script': "run-tests.py"}],
    zipfile=None, requires=['py2exe']
)
