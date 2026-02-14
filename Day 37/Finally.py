"""
Finally clause -> The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

Syntax ->
try:
    # statements which could generate exception
except:
    # solution of generated exception
finally:
    # block of code which is going to execute in any situation
"""

def func1():
    try:
        l = [1, 5, 3, 8, 4]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("Finally code executed")

x = func1()
print(x)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a / b
    print(c)
except Exception as e:
    print(e)
finally:
    print("Finished the execution with the finally block")
