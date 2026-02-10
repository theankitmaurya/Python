"""
Match Case Statements:
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language, you must have heard of switch -case statements.

A match statement will compare a given variable's value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all present patterns until it fits into one.

The match case consists of three main entities:
1. The match keyword
2. One or more clauses
3. Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.
"""

x = int(input("Enter a number: "))

match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _:
        print(x)
