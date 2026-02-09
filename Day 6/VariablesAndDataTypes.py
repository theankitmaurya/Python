# Variable - Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc. Creating a variable is like creating a placeholder in memory and assigning it some value. In python its easy as writing:

a = 1
b = "Ankit"
c = True
d = None


# These are four variables of different data types.

"""
What is a Data Type ?
Data Type specifies the type of value a variable holdx. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function.
"""

a = 1
print(type(a))
b = "1"
print(type(b))

"""
1. Numeric Data: int, float, complex
int: 3, -6, 0
float: 4.565, 0.00003
complex: 3 + 5i
"""

p = 5 # this is an int
q = 5.75 # this is a float
r = complex(5, 8) # this is a complex number

print (p, q, r)

"""
Text Data: str
str: "Hello World", "Python Programming"
"""

print("Hello World", "Python Programming")

"""
Boolean Data: Consists of values True or False.
"""

a = True
b = False
print(a, b)

"""
Sequenced Data: list, tuple
list: A list is an ordered collection of data with elements separated by a  comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parenthesis. Tuples are immutable and cannot be modified after creation.
"""

list1 = [3, 5.6, [-4, 2.3], ["banana", "grapes"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

"""
Mapped Data: dict
dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
"""

dict1 = {"name":"Ankit", "age":"20", "canVote":True}
print(dict1)

