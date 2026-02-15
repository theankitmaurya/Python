"""
Local and Global Variables -> As we know a variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator =.
"""

x = 5
print(x)

"""
A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.

On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in our code.
"""

x = 10 # global variable

def func():
    y = 5 # local variable
    print(y)

func()
print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

"""
In this example, we have a global variable x and a local variable y. We can access the value of the global variable x from within the function, but we cannot access the value of the local variable y outside of the function.
"""

"""
The global keyword -> The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope.
"""

x = 10
print(x)

def func():
    global x
    x = 5
    y = 6

func()
print(x)

"""
Tn this example, we used the global keyword to declare that we want to modify the global variable x from within the function. As a result, the value of x is changed to 5.

It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make our code harder to debug.
"""
