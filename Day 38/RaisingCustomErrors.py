"""
Raising Custom Errors -> In python, we can raise errors by using the 'raise' keyword.
We know about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.
"""

a = int(input("Enter a number between 2 and 8: "))
if (a < 2 or a > 8):
    raise ValueError("Value is not between 2 and 8")

"""
Defining Custom Exceptions -> In python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.
This is useful because sometimes we might want to do something when a particular exception is raised.

Syntax:
class CustomError(Exception):
    # code ...
    pass
try:
    # code ...
except CustomError:
    # code ...
"""
