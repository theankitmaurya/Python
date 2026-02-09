# Module is a code library which can be used to borrow the code written by somebody else in our python program. There are two types of modules in python:

# (1) Built in Modules - These modules are ready to import and use and ships with the python interpreter. There is no need to install such modules explicitly.
#  Ex -
import hashlib

# (2) External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.
# Ex -
import pandas

# The pip command -
# It can be used as a package manager pip to install a python module. To install module called tensorflow using the command: pip install tensorflow

# Using a module in Python(Usage) -
# We use the import syntax to import a module in Python. Here is an example code.
import pandas

# Read and work with a file named 'words.csv'
pandas.read_csv('words.csv')
