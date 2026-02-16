"""
Lambda Functions in Python -> in Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:

lambda arguments : expression

Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter and reduce.
"""

def double(x):
    return x * 2

double = lambda x : x * 2
print(double(5))

"""
The above lambda function has the same functionality as the double function defined earlier. However, the lambda function is anonymous, as it does not have a name.
Lambda functions can have multiple arguments, just like regular functions.
"""

avg = lambda x, y, z: (x + y + z) / 3
print(avg(5, 10, 15))

"""
Lambda Functions can also include multiple statements, but they are limited to a single expression.
"""

ab = lambda x, y : print(f"{x} * {y} = {x * y}")
