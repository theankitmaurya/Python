"""
While Loop -> As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.
"""

i = 0
while (i < 10):
    print(i)
    i += 1

"""
Else with While Loop -> We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.
"""

x = 5
while (x > 0):
    print(x)
    x -= 1
else:
    print("Count is 0")
