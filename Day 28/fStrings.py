"""
String formatting in Python -> String formatting can be done using the format method.
"""

txt = "For only {price:.2f} rupees"
print(txt.format(price = 49.567567))

"""
f-strings in python -> It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f-character preceding the string literal). the primary focus of this mechanism is to make the interpolation easier.
When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.
"""

name = input("Enter your name: ")
country = input("Enter you country: ")
letter = f"Hey my name is {name} and I am from {country}"

print(letter)
