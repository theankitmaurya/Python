"""
Python Tuples -> Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets(). Tuples are unchangeable meaning we can not alter them after creation.
"""

tup = (1, 3, 4, 6, 8, 2, 8, 5)
print(tup)
print(type(tup))

"""
Tuples Indexes -> Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.
"""

print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])

"""
Accessing Tuple items:
1. Positive Indexing: As we have seen that tuple items have index, as such we can access items using these indexes.
"""

print(tup[0])

"""
2. Negative Indexing: Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.
"""

print(tup[-1])
print(tup[-2])
print(tup[-3])
print(tup[-4])

"""
3. Check for item: We can check if a given item is present in the tuple. This is done using the 'in' keyword.
"""

if 4 in tup:
    print("4 is present")
else:
    print("4 is not present")


"""
Range of Index -> We can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

Syntax: Tuple[start : end : jumpIndex]
Note: jumpIndex is optional.
"""

tup2 = tup[1 : 4]
print(tup2)
