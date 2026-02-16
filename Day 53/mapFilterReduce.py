"""
Map, Filter and Reduce -> In Python, the map, filter and reduce functions are built-in functions that allow us to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.
"""

"""
map() -> The map() function applies a function to each element in  a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

map(function, iterable)
"""

def cube(x):
    return x * x * x

print(cube(2))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newl = list(map(cube, l))
print(newl)

newl = list(map(lambda x : x * x * x, l))
print(newl)

"""
In the above example, the lambda function lambda x : x * x * x is used to cube each element in the numbers list. The map function applies the lambda function to each element in the list and returns a new list containing the cube of the original numbers.
"""

"""
filter() -> The filter() function filters a sequence of elements based on a given predicate(a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

filter(predicate, iterable)

The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple or any other iterable object.
"""

def FilterFunc(a):
    return a > 4

newl = list(filter(FilterFunc, l))
print(newl)


newl = list(filter(lambda x : x > 4, l))
print(newl)

"""
In the above example, the lambda function lambda x : x > 4 is used to filter the numbers list and return only the number greater than 4. The filter function applies the lambda function to each element in the lost and returns a new list containing only numbers greater than 4.
"""

"""
reduce() -> The reduce() function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

reduce(function, iterable)

The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as lost or tuple.

The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.
"""

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y : x + y, numbers)

print(sum)

"""
In the above example, the reduce() function applies the lambda function lambda x, y : x + y to the elements in the number list. The lambda function adds the two arguments x and y and returns the result. The reduce function applies the lambda function to the first two elements in the list (1 and 2), then applies the function to the result (3) and the next element (3) and so on. The final result is sum of all the elements in then list, which is 15.
"""

# Note -> It is important to note that the reduce function requires the functools module to be imported in order to use it.
