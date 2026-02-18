"""
Python Class and Objects -> A class is a blueprint or a template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

Creating a class -> Let us now create a class using the class keyword.
class Details:
    name = "Rohan"
    age = 20

Creating an Object -> Object is the instance of the class used to access the properties of the class.
obj1 = Details()
"""

class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person()
print(a.name, a.occupation, a.networth)
a.name = "Shubham"
a.occupation = "Accountant"
a.info()

"""
self Parameter -> The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
"""

class Details:
    name = "Anmol"
    age = 17

    def desc(self):
        print("My name is", self.name, "and I am", self.age, "years old.")

obj1 = Details()
obj1.desc()

obj2 = Details()
obj2.name = "Ankit"
obj2.age = 20
obj2.desc()
