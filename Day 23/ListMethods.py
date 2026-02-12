# List Methods ->

l = [11, 4, 46, 27, 2, 78, 5, 5, 3, 87]
print(l)


# 1. list.sort() -> This method sorts the list in ascending order. The original list is updated. If we want to print the list in descending order then we must give reverse = True as a parameter in the sort method
l.sort()
print(l)

l.sort(reverse = True)
print(l)

# 2. reverse() -> This method reverses the order of the list
l.reverse()
print(l)

# index() -> This method returns the index of the first occurrence of the list item.
print(l.index(4))

# count() -> returns the count of the number of items with the given value.
print(l.count(5))

# copy() -> Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
l1 = l.copy()
l1[0] = 0
print(l1)

# append() -> This method appends items to the end of the existing list.
l.append(24)
print(l)

# insert() -> This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
l.insert(1, 23)
print(l)

# extend() -> This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
m = [45, 67, 30]
l.extend(m)
print(l)


"""
Concatenating two lists: You can simply concatenate two lists to join two lists.
"""

m = [45, 67, 30]
k = l + m
print(k)
