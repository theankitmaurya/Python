"""
String Methods - Python provides a set of built-in methods that we can use to alter and modify the strings.
"""

# upper() -> The upper method converts a string to upper case.
str1 = "AbcDEfghIJ"
print(str1.upper())

# lower() -> The lower() methods converts a string to lower case.
str1 = "AbcDEfghIJ"
print(str1.lower())

# strip() -> The strip() method removes any white spaces before and after the string.
str2 = " Hello, Ankit "
print(str2.strip())

# rstrip() -> The rstrip() removes any trailing characters.
str3 = "Ankit!!!!!!!"
print(str3.rstrip("!"))

# replace() -> The replace() method replaces all occurrences of a string with another string
str4 = "Ankit"
print(str4.replace("Ankit", "Sam"))

# split() -> The split() method splits the given string at the specified instance and returns the separated strings as list items.
str5 = "Ankit is a good boy"
print(str5.split())

# capitalize() -> The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
str6 = "ankit"
print(str6.capitalize())

# center() -> The center() method aligns the string to the center as per the parameters given by the user.
str7 = "Welcome back user!!!"
print(len(str7))
print(str7.center(50))
print(len(str7.center(50)))

# We can also provide padding character. It will fill the rest of the fill characters provided by the user.
print(str7.center(50, "."))

# count() -> The count() method returns the number of times the given value has occurred within the given string
str8 = "Mathematics"
print(str8.count("a"))

# endswith() -> The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str9 = "Welcome to the new World!!!!"
print(str9.endswith("!"))

# We can even also check for a value in-between the string by providing start and end index positions
print(str9.endswith("to", 4, 10))

# find() -> The find() method searches for the first occurrence of the given value and returns the index where it is present. If the given value is absent from the string then return -1
str10 = "He's name is Ankit. He is a honest man."
print(str10.find("is"))

# index() -> The index method searches for the first occurrence of the given value and returns the index where it is present. Ig given value is absent from the string then raise an exception.
str11 = "He's name is Ankit. He is a honest man."
# print(str11.index("isa"))

# isalnum() -> The isalnum() method returns True only if the entire string only consists og A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False
str12 = "WelcomeToTheTerminal"
print(str12.isalnum())

# isalpha() -> The isalpha() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False
str13 = "WelcomeToTheTerminal00"
print(str13.isalpha())

# islower() -> the islower() method returns True if all the characters in the string are lower case, else it returns False
str14 = "hello world"
print(str14.islower())

# isprintable() -> The isprintable() method returns True if all the values within the given string are printable, if not, then return False
str15 = "Hello! how are you"
print(str15.isprintable())

# isspace() -> The isspace() method returns True only and only if the string contains white spaces, else returns False
str16 = "   "
print(str16.isspace())


# istitle() -> The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False
str17 = "To kill a mocking bird"
print(str17.istitle())

# isupper() -> The isupper() method returns True if all the characters in the string are upper case, else it returns False
str18 = "WORLD HEALTH ORGANIZATION"
print(str18.isupper())

# startswith() -> The startswith() method checks if the string starts with a given value. If yes then return True, else return False
str19 = "Python is a very nice language"
print(str19.startswith("Python"))

# swapcase() -> The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case
str20 = "Python Is An Interpreted Language"
print(str20.swapcase())

# title() -> The title() method capitalizes each letter of the word within the string
str21 = "His name is Ankit. He is a good boy"
print(str21.title())
