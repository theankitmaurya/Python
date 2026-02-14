"""
How importing in Python works -> Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

To import a module in PYthon, we can use the import statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, we would use 'import math' statement.
"""

import math

"""
Once a module is imported, we can use any of the functions and variables defined in the module by using dot notation. For example, to use the sqrt function from the math module:
"""

print(math.sqrt(9))

"""
from keyword -> We can also import specific functions or variables from a module using the from keyword. We can also import multiple functions or variables at once by separating them with a comma. For example, to import only the sqrt and pi function from the math module:
"""

from math import sqrt, pi
print(sqrt(9) * pi)

"""
Importing everything -> It's possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to i=understand where specific functions and variables are coming from.
"""

from math import *
print(sqrt(9))
print(pi)

"""
The 'as' keyword -> Python also allows us to rename imported modules using the as keyword. This can be useful if we want to use shorter or more descriptive name for a module, or if we want to avoid naming conflicts with other modules or variables in our code.
"""

import math as m
print(m.sqrt(9))

"""
The dir function -> Finally, Python has a built-in function called dir that we can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.
"""

print(dir(math))

"""
This will output a list of all the names defined in the math module, including functions like sqrt and pi, as well as other variables and constants.

In summary, the import statement in Python allows us to access the functions and variables defined in a module from within our current script. We can import the entire module, specific functions or variables, or use the * wildcard to import everything. We can also use the as keyword to rename a module, and the dir function to view the contents of a module.
"""
