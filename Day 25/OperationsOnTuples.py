"""
Manipulating Tuples -> Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
"""

countries = ("Spain", "Russia", "India", "China", "Germany", "Indonesia")
temp = list(countries)
print(type(temp))
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

"""
Thus, we can convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.
However, we can directly concatenate two tuples without converting them to list.
"""

countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "Sri Lanka")
countries2 = ("Vietnam", "France", "USA")

country = countries1 + countries2
print(country)


"""
Tuple Methods -> As tuple is immutable type of collection of elements it have limited built in functions.
"""

# count() -> The count() method of Tuple returns the number of times the given element appears in the tuple.

tup = (0, 2, 4, 6, 8, 10)
res = tup.count(4)
print("Count of 4:", res)

# index() -> the index() method returns the first occurrence of the given element from the tuple.
# Syntax: tuple.index(element, start, end)
# This method raises a ValueError if the element is not found in the tuple.

res = tup.index(10)
print(res)
