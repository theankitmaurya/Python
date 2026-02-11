"""
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types:
(1) for loop
(2) while loop
"""

"""
The for loop -> for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.
"""

# Iterating over a string:
name = "Ankit"
for i in name:
    print(i)

# Iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow", "Orange"]
for color in colors:
    print(color)

# range() -> What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

for k in range(5):
    print(k)

for k in range(0, 11):
    print(k)
