"""
Docstrings in Python -> Python docstrings are the literals that appear right after the definition of a function, method, class or module.
"""

"""
Python comments vs Docstrings ->
1. Python Comments -> Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

2. Python docstrings -> As mentioned above, Python docstrings are strings used right after the definition of a function, method, class or module. They are used to document our code.
We can access these docstrings using the doc attribute.
"""

"""
Python doc attribute -> Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.
"""

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n ** 2)

square(6)
print(square.__doc__)

"""
PEP 8 -> PEP 8 is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for python and documents aspects of Python, like design and style, for the community.
"""

"""
The ZEN of Python -> Long time Pythoneer Tim Peters succinctly channels the BDFL's guiding principles for python's design into 20 aphorisms, only 19 of which have been written down.

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.     
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.       
Namespaces are one honking great idea -- let's do more of those!     
"""
