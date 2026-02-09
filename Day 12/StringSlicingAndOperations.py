"""
String Slicing & Operations on String:

Length of a String - We can find the length of a string using len() function.
"""

books = "Mathematics"
len1 = len(books)
print("Mathematics is a", len1, "letter word")

"""
String as an array - A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.
"""

pie = "Applepie"
print(pie[0 : 4]) # prints the string from including index 0 till excluding the index 4
print(pie[ : 7])
print(pie[ : ])
print(pie[2 : -2])
print(pie[ : -3])
print(pie[ : len(pie) - 3])
