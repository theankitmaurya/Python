"""
Python - else in Loop ->
As we know, the else clause is used along with the if statement.
Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. the statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.
"""

for i in range(4):
    print(i)
else:
    print("Completed")


for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Completed")

# if we used break in for-else loop then the else code wo't get executed.
