"""
Python Lists ->
1. Lists are ordered collection of data items.
2. They store multiple items in a single variable.
3. List items are separated by commas and enclosed within square brackets [].
4. Lists are changeable meaning we can alter them after creation.
"""

marks = [3, 5, 6]
print(marks)
print(type(marks))

"""
List Index -> Each item/element in a list has its own unique index. This index an be used to access any particular item from the list. The first item has index [0], second item has index [1], the third item has index [2] and so on.
"""

print(marks[0])
print(marks[1])
print(marks[2])

"""
Accessing list items -> We can access list items by using its index with the square bracket syntax [].
"""

"""
Positive Indexing: As we have seen that list items have index, as such we can access items using these indexes.
"""

print(marks[0])
print(marks[2])

"""
Negative Indexing -> Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. the last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.
"""

print(marks[-1])
print(marks[-2])
print(marks[-3])


"""
Check whether an item in present in the list?
We can check if a given item is present in the list. This is done using the 'in' keyword.
"""

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present")
else:
    print("Yellow is absent")

"""
Range of index -> You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

Syntax: listName[start : end : jumpIndex]

Note: jump Index is optional.
"""

marks = [3, 5, 6, 8, 2, 9, 0, 2, 4, 6, 4, 2]
print(marks)
print(marks[:])
print(marks[1:9])
print(marks[1:9:2])

"""
Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.

Note: The element of the end index provided will not be included.

When no end index is provided, the interpreter prints all the values till the end.
"""

"""
List Comprehension -> List comprehension are used for creating new lists from other iterables like lists, tuples, dictionaries, sets and even in arrays and strings.

Syntax: List = [Expression(item) for item in iterable if condition]

Expression: it is the item which is being iterated.

Iterable: It can be list, tuples, dictionaries, sets and even in arrays and strings.

Condition: Condition checks if the item should be added to the new list or not.
"""

lst = [i * i for i in range(10)]
print(lst)

lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)
