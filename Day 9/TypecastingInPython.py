"""
Typecasting in Python - The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict() etc. for the type casting in python.

Two types of Typecasting:
(1) Explicit Conversion (Explicit type casting in python)
(2) Implicit Conversion (Implicit type casting in python)
"""

"""
Explicit Typecasting:
THe conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.
It can be achieved with the help of python's built-in type conversion functions such as int(), float(), hex(), oct(), str() etc.
"""
# Examples of explicit typecasting:
string = "15"
number = 2
string_number = int(string)
sum = number + string_number
print(sum)

"""
Implicit Typecasting:
Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the python interpreter itself(automatically). This is called implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.
"""
# Examples of implicit typecasting:
a = 7
b = 5.7
print(a + b)
