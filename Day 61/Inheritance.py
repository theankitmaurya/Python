"""
Inheritance in Python -> When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods, this is called as inheritance.
"""

"""
Python Inheritance Syntax -> Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.
"""

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee is {self.name} and has id {self.id}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")

e1 = Employee("Rohan Das", 45)
e1.showDetails()

e2 = Programmer("Ankit", 1)
e2.showDetails()
e2.showLanguage()

"""
Types of Inheritance ->
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchial Inheritance
5. Hybrid Inheritance
"""
