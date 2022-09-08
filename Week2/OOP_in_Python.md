# OOP in Python
* In Python, object-oriented Programming (OOP) is a programming model that uses objects and classes in programming.
* It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. 
* The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.
# Class
* A class is a collection of objects.
* A class contains the blueprints or the prototype from which the objects are being created. 
* It is a logical entity that contains some attributes and methods.
* Classes are created by keyword class.
* Attributes are the variables that belong to a class  & are always public and can be accessed using the dot (.) operator.
```python
class Dog:
```
# Object
* The object is an entity that has a state and behavior associated with it. 
* It may be any real-world object like a mouse, keyboard, chair, table, pen, etc. 
* Integers, strings, floating-point numbers, even arrays, and dictionaries, are all objects.
* The number 12 is an object, the string “Hello, world” is an object, a list is an object that can hold other objects, and so on.
 ### An object consists of :

* **State:** It is represented by the attributes of an object. It also reflects the properties of an object.
* **Behavior:** It is represented by the methods of an object. It also reflects the response of an object to other objects.
* **Identity:** It gives a unique name to an object and enables one object to interact with other objects.
```python
obj = Dog()
```
# Self Method &  ```__init__``` Method
* Class methods must have an extra first parameter in the method definition. 
* The self is used to represent the instance of the class. 
* With this keyword, you can access the attributes and methods of the class in python.
* The `__init__` method is similar to constructors in C++ and Java.
* It is run as soon as an object of a class is instantiated. 
* The method is useful to do any initialization you want to do with your object. 
```
python
class Customer:
    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
        print("customer created")
```
# Creating Class and objects with methods
```python
class Customer:
    def __init__(self,name,membership_type):
        self.name=name
        self.membership_type=membership_type
        print("customer created")
    def update_membership(self,new_membership):
        print("Calculating costs")
        self.membership_type=new_membership
    def __str__(self):
        return self.name +" "+self.membership_type
    def print_all_customers(customers):
        for customer in customers:
            print(customer)
    def __eq__(self,other):
        if self.name==other.name and self.membership_type==other.membership_type:
            return True
        return False
customers=[Customer('Farhan','Silver'),Customer('Haider','Gold')]
print(customers[0].name)
Customer.print_all_customers(customers)
print(customers[0]==customers[1])
```
# `__hash__` method
* The hash() function accepts an object and returns the hash value as an integer.
* When you pass an object to the hash() function, Python will execute the __hash__ special method of the object.
* If we write `__hash__=None` then generate error after creating dictionary of objects of person ``` TypeError: unhashable type: 'Person' ```
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def age(self):
        return self.age

    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)
members = {
    Person('John', 22),
    Person('Jane', 22)
}
```
# `__repr__` vs `__str__` Method
* The __str__ method returns a string representation of an object that is human-readable while the __repr__ method returns a string representation of an object that is machine-readable.

```python
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'Person("{self.first_name}","{self.last_name}",{self.age})'

    def __str__(self):
        return f'({self.first_name},{self.last_name},{self.age})'


person = Person('John', 'Doe', 25)
# use str()
print(person)

# use repr()
print(repr(person))
```
```
Output
(John,Doe,25)
Person("John","Doe",25)
```
# Encapsulation
* Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
* It describes the idea of wrapping data and the methods that work on data within one unit. 
* This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.
* To prevent accidental change, an object’s variable can only be changed by an object’s method.
* Those types of variables are known as private variables.
```python
class Base:
    def __init__(self):
        self.a="Python"
        self.__c="Python"
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class:")
        print(self.__c)
obj1=Base()
print(obj1.a)
obj2=Derived()
print(obj2)
```
* It through error because we cannot even access this attribute directly and can’t even change its value.
* To resolve this issue, we use getters & setters to add validation logic around getting and setting a value
* Using @property decorators to achieve getters and setters behaviour.
```python
class Base:
    def __init__(self):
        self.a="Python"
        self.__c="Python"
    @property
    def name(self):
        return self.__c
    @name.setter
    def name(self,n):
        self.__c=n
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of base class:")
        print(self.name)
obj1=Base()
print(obj1.name)
obj2=Derived()
obj2.name='Coding'
print(obj2.name)
```
# Inheritance
* Inheritance is the capability of one class to derive or inherit the properties from another class. 
* The class that derives properties is called the derived class or child class and the class from which the properties are being derived is called the base class or parent class.
* It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
* **Single-level** inheritance enables a derived class to inherit characteristics from a single-parent class.
* **Multi-level** inheritance enables a derived class to inherit properties from an immediate parent class which in turn inherits properties from his parent class.
* **Hierarchical** level inheritance enables more than one derived class to inherit properties from a parent class.
* **Multiple level** inheritance enables one derived class to inherit properties from more than one base class.
```python
class person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
class Employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,idnumber)
    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))
a=Employee("Farhan",2340,245000,'Intern')
a.display()
a.details()
```
# Polymorphism
* Polymorphism simply means having many forms. 
* It means that the same function name (but different signatures) being used for different types.
```python
class Bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")
class sparrow(Bird):
    def flight(self):
        print("sparrow can fly")
class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
obj_bird.intro()
obj_bird.flight()
obj_spr.intro()
obj_spr.flight()
obj_ost.intro()
obj_ost.flight()
```
# Abstraction
* It hides the unnecessary code details from the user.
* Also, when we do not want to give out sensitive parts of our code implementation and this is where data abstraction came.
* Data Abstraction in Python can be achieved through creating abstract classes.
* Python comes with a module that provides the base for defining Abstract Base classes(ABC) and that module name is ABC.
```python
from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")
t= Tesla()
t.mileage()
d = Duster()
d.mileage()
```















