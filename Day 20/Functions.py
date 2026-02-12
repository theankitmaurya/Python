"""
Python Functions -> A function is a block of code that performs a specific task whenever it is called. In bigger problems, where we have large amount of codes, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:
1. Built-in functions
2. User-defined functions
"""

"""
Built-in Functions -> These functions are defined and pre-coded in python. Some exapmles of built-in functions are as follows:
min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print()
"""

"""
User defined Functions -> We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

Syntax ->
1. Create a function using the def keyword., followed by a function name, followed by a paranthesis (()) and a colon(:).
2. Any parameters and arguments should be placed within the paranthesis.
3. Rules to naming function are similar to that of naming variables.
4. Any statements and other code within the function should be intended.

Calling a Function -> We call a function by giving the function name, followed by parameters (if any) in the paranthesis.
"""

def isGreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater")

a = 34
b = 38
isGreater(a, b)

c = 3
d = 2
isGreater(c, d)

def isLesser(a, b):
    pass

# pass -> when we create a function and don't write any code inside it then the function will give an error. So to bypass the error ewe will use pass keyword.

