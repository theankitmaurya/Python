"""
Break Statement -> The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.
"""

for i in range(1, 101, 1):
    print(i, end = " ")
    if (i == 50):
        break
    else:
        print("Mississippi")
print("Thank you")


for i in range(12):
    if (i == 10):
        break
    print("5 X", i + 1, "=", 5 * (i + 1))

"""
Continue Statement -> The continue statement skips the rest of the loop statements and causes the next iteration to occur.
"""

for i in range(1, 50):
    if (i == 10):
        continue
    print(i, end = " ")
