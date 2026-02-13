"""
Joining Sets -> Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.
"""

"""
1. union() and update() -> The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.
"""

s1 = {1, 2, 4, 6, 8}
s2 = {3, 2, 6, 9, 7}

print(s1.union(s2))
print(s1, s2)

s1.update(s2)
print(s1, s2)

"""
2. intersection() and intersection_update() -> The intersection() and intersection_update() method prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
"""

cities1 = {"Tokyo", "Rio", "Paris", "Delhi", "Beijing"}
cities2 = {"Tokyo", "California", "Germany", "Paris"}
print(cities1.intersection(cities2))

"""
3. symmetric_difference() and symmetric_difference_update() -> The symmetric difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
"""

print(cities1.symmetric_difference(cities2))

"""
4. difference() and difference_update() -> The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
"""

print(cities1.difference(cities2))

# Set Methods -> There are several in-built methods used for the manipulation of set.

# 1. isdisjoint() -> The isdisjoint() method checks if items of given set are present in another set. This returns False if items are present, else it returns True.
print(cities1.isdisjoint(cities2))

# 2. issuperset() -> The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
print(cities1.issuperset(cities2))

# 3. issubset() -> The subset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
print(cities2.issubset(cities1))

# 4. add() -> If you want to add a single item to the set use the add() method
cities1.add("Bali")
print(cities1)

# 5. update() -> If we want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary) and use the update() method to add it into the existing set.
cities1.update(cities2)
print(cities1)

# 6. remove()/discard() -> We can use remove() and discard() methods to remove items from list.
# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
cities1.remove("Bali")
print(cities1)

# 7. pop() -> This method removes the last item of the set but the catch is that we don't know which item gets popped as sets are unordered. However, we can access the popped item if we assign the pop() method to a variable.
item = cities1.pop()
print(cities1)
print(item)

# 8. clear() -> this method clears all items in the set and prints an empty set.
cities2.clear()
print(cities2)

# del -> del is not a method, rather it is a keyword which deletes the set entirely.
del cities2
# print(cities2)

"""
Check if an item exists -> We can also check if an item exists in the set or not.
"""

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
