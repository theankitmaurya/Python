"""
seek() and tell() functions -> In Python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in on module, which provides a consistent interface for reading and writing to various file-like objects, such as files, pipes and in-memory buffers.
"""

"""
seek() function -> The seek() function allows us to move the current position within a file to a specific point. Th position is specified in bytes and we can move either forward or backward from the current position.
"""

with open("file.txt", "r") as f:
    f.seek(10)

    data = f.read(5)
    print(data)

"""
tell() function -> The tell() function returns the current position within the files, in bytes. This can be useful for keeping track of uor location within a file or for seeking to a specific position relative to the current position.
"""

with open("file.txt", "r") as f:
    f.seek(10)

    print(f.tell())
    data = f.read(5)
    print(data)

"""
truncate() function -> When we open a file in Python using the open function, we can specify the mode in which we want to open the file. If we specify the ode as 'w' or 'a', the file is opened in write mode and we can write to a file. However, if we want to truncate the file to a specific size, we can use the truncate function.
"""

with open("file.txt", "w") as f:
    f.write("Hello World!")
    f.truncate(5)


with open ("file.txt", "r") as f:
    print(f.read())

