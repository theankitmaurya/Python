# Dictionary Methods -> Dictionary uses several built-in methods for manipulation.

# 1. update() -> The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

ep1 = {121 : 23, 122 : 65, 123 : 89, 124 : 43}
ep2 = {221 : 60, 222 : 90, 223 : 99, 224 : 56, 225 : 15}

ep1.update(ep2)
print(ep1)

# 2. clear() -> The clear() method removes all the items from the list.
ep1.clear()
print(ep1)

# 3. pop() -> The pop() method removes the key-value pair whose key is passed as a parameter.
ep2.pop(221)
print(ep2)

# 4. popitem() -> The popitem() method removes the last key-value pair from the dictionary.
ep2.popitem()
print(ep2)

# del -> We can also use the del keyword to remove a dictionary item. if key is not provided, then the del keyword will delete the dictionary entirely.
del ep2[222]
del ep2
