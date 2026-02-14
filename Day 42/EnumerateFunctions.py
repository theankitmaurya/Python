"""
Enumerate Function in Python -> The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple or string) and get the index and value of each element in the sequence at the same time.
"""

marks = [10, 56, 34, 99, 23, 89, 45, 52]

for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Awesome! Ankit")

"""
As we can see the enumerate function returns a tuple containing the index and value of each element in the sequence. We can use the for loop to unpack these tuples and assign them to variables.
"""

"""
Changing the start index -> By default, the enumerate function starts the index at 0, but we can specify a different starting index by passing it as an argument to the enumerate function.
"""

for index, mark in enumerate(marks, start = 1):
    print(mark)
    if (index == 3):
        print("Awesome! Ankit")

"""
the enumerate function is often used when we need to loop over a sequence and perform some action with both index and value of each element.
"""
