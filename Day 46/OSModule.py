"""
os Module in Python -> The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows us to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

Some common tasks we can perform with the os module:
Reading and writing files: The os module provides functions for opening, reading and writing files.
"""

import os

if (not os.path.exists("data")):
    os.mkdir("data")

for i in range(0 ,5):
    os.mkdir(f"data/Days {i + 1}")
    os.rename(f"data/Days {i + 1}", f"data/Tutorials {i + 1}")

folders = os.listdir("data")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
