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

"""
Do-while Loop -> do while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at hte end of the while loop. It is also known as an exit-controlled loop.

How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapper in an if statement that checks a given condition and breaks the iteration if that condition becomes True.
"""

i = 0
while True:
    print(i)
    i = i + 1
    if (i % 100 == 0):
        break
    
