"""
Python Sets -> Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.
"""

info = {2, 4, 6, 8, 10, 5, 2, 8, 4, 7, 9}
print(info)

"""
Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets do not allow duplicate values.
"""

ankit = set() # To see the type of any empty set we have to write like this
print(type(ankit))

"""
Accessing set items: Using a for loop -> We can access items of set using a for loop.
"""

for item in info:
    print(item)
