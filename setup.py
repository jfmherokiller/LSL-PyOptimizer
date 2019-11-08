from setuptools import setup, find_packages
import py2exe
import sys
import os

#sys.argv.append('py2exe')
Mydata_files = [('.', ['builtins.txt', 'fndata.txt'])]
setup(
    data_files=Mydata_files,
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    console=[{'script': "main.py"}, {'script': "run-tests.py"}],
    zipfile=None, requires=['py2exe'],
    python_requires='>=2.7,<3.0',
    name='LSL-Optimizer',
    version="0.1",
    packages=find_packages(),
    scripts=['main.py', 'run-tests.py'],

    include_package_data=True,
    url='https://github.com/Sei-Lisa/LSL-PyOptimizer'
)
