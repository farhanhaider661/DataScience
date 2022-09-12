# Modules: 
* Modules refer to a file containing Python statements and definitions.
* A module’s contents are accessed with the import statement.
* It is any Python files with a .py extension. It can be imported into python without the .py part.
* A file containing Python code, for example: example.py, is called a module, and its module name would be example.

**example.py**
```python
def add(a,b):
    result=a+b
    print(result)
```
**main.py**
```python
# We use the import keyword to do this. To import our previously defined module example, we type the following in the Python prompt.
import  example
# Using the module name we can access the function using the dot . operator. For example:
example.add(3,4)
```
# Pakages:
* A Python package is nothing but a collection of modules along with a `__init__.py` file.
*  The modules can also be arranged in hierarchy of folders inside a package.
*  Just by adding an empty` __init__.py` file to the in the folder, Python knows it is a Package.
*  In fact, a package is also really a module that contains other modules.

![image](https://user-images.githubusercontent.com/111038642/189672990-bc844e1a-eb66-4efd-87b0-d2adbb221f08.png)

**main.py**
```python
from pkg import A,B
A.first()
B.second()
```
# Conclusion:
* The module is a simple Python file that contains collections of functions and global variables and with having a .py extension file. 
* The package is a simple directory having collections of modules
