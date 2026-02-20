"""
Python Dictionaries -> Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.
"""

dic = {'name': 'Ankit', 'age': 20, 'eligible': True}
print(dic)

"""
Accessing Dictionary Items:
1. Accessing Single Values -> Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
"""

print(dic['name'])
print(dic.get('name'))

"""
2. Accessing Multiple Values -> We can print all the values in the dictionary using values() method.
"""

print(dic.values())

for key in dic.keys():
    print(dic[key])

"""
3. Accessing keys -> We can print all the keys in the dictionary using keys() method.
"""

print(dic.keys())

"""
4. Accessing key-value pairs -> We can print all the key-value pairs in the dictionary using items() method.
"""

print(dic.items())
for key, value in dic.items():
    print(key, ":", value)
