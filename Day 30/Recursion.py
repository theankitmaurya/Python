"""
Recursion in Python -> Recursion is the process of defining something in terms of itself.
"""

"""
Python Recursive Functions -> In python, we know that a function can call other functions. It is even possible for the functions to call itself. These types of construct are termed as recursive functions.
"""

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
