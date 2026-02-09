"""
What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
"""

name = "Ankit"
print("Hello,", name)

"""
NOTE: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.
"""

name = "Ankit"
name = 'Ankit'

"""
Sometimes, the user might need to put quotation marks in between the strings.
"""

print('He said, "I want to eat an apple."')

"""
Multiline Strings - If our string has multiple lines, we can create them like this:
"""

a = """He said,
I am very,
good in English"""

print(a)

"""
Accessing Characters of a String -
In python, strings is like an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.
"""

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5]) # this throws an error as 5th index doesn't exist in name

"""
Looping through the String -
We can loop through strings using a for loop like this:
"""

for character in name:
    print(character)
