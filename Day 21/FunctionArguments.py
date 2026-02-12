"""
Function Arguments and return statement -> There are four types of arguments that we can provide in a function:
1. Default Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required Arguments
"""

"""
Default Arguments -> we can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.
"""

def average(a = 9, b = 1):
    print(" The average is", (a + b) / 2)

average()
average(4)
average(b = 9)
average(4, 9)

"""
Keyword Arguments -> We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the order in which the arguments are passed does not matter.
"""

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")

"""
Required Arguments -> In case we don't pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order number and the number of arguments passed should match with actual function definition.
"""

def gmean(a, b, c = 1):
    print((a * b * c) / (a + b * c))

gmean(2, 4)


"""
Variable length Arguments -> Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:
1. Arbitrary Arguments: While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.
"""

def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Average is:", sum / len(numbers))

average(5, 8, 5, 3)

"""
2. Keyword Arbitrary Arguments: While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.
"""

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Peter", fname = "Jade", lname = "Watson")


"""
return statement -> the return statement is used to return the value of the expression back to the calling function.
"""

def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)

c = average(4, 5, 6, 7)
print(c)
