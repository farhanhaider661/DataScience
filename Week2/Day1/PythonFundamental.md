# Python 
* Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.
# Variables using input()
```
age=input("Enter your age: ")
print(age)
```
![image](https://user-images.githubusercontent.com/111038642/188460652-fbd62eb9-840d-4ecf-9cec-b71347c5e3fe.png)
# Type Conversions
```
birth_year=int(input('Enter your Birth Date:'))
Age=2022-birth_year
print("Age:"+str(Age))
```
![image](https://user-images.githubusercontent.com/111038642/188461078-9af16cdb-652b-44f8-acf6-6c1cc1cfb4f6.png)
# String Methods
```
Course='python is programming language'
print(Course.upper())
print(Course.find('is'))
print(Course.replace('programming','fun'))
print('python' in Course)
```
![image](https://user-images.githubusercontent.com/111038642/188461864-7004b54c-573a-43c8-ba15-9e4aa813ef49.png)
# Operators Precedence
```
x=(10+3*(12-8)**2)//3
print(x)
```
![image](https://user-images.githubusercontent.com/111038642/188462517-4ccde6a4-c387-4826-9aae-6592907b66c5.png)
# Comparison & Logical Operators
```
x=3>2
print(x)
y=12<=12
print(y)
price=124
print(price >125 and price <136)
print(price >125 or price <136)
print(not price >10)
```
![image](https://user-images.githubusercontent.com/111038642/188463121-f24fa2f1-7204-4a8e-8f91-1ba3c7b3b14b.png)
# If Else Statement
```
Weight=int(input('Enter Weight: '))
Unit=input("(K)g or (L)bs: ")
if Unit.upper() =='K':
    convert=Weight/0.45
    print("Weight in Lbs:"+ str(convert))
elif Unit.upper() =='L':
    convert=Weight *0.45
    print("Weight in Kg:"+ str(convert))
else:
    print('Unit is wrong')
```
![image](https://user-images.githubusercontent.com/111038642/188466194-e9b63fe7-271e-466d-b810-c1bf6fc91505.png)
# whileloop
```
i=1
while i <=6:
    i=i+2
    print(i)
```
![image](https://user-images.githubusercontent.com/111038642/188466917-2c3d2053-29ac-4dab-ac61-cad97d568c02.png)
# List Methods
```
Marks=[90,94,87,81,85]
Marks.append(89)
print(Marks)
Marks.insert(0,100)
print(Marks)
Marks.clear()
print(Marks)
```
![image](https://user-images.githubusercontent.com/111038642/188467706-e5f6e948-236b-4634-9887-4b48b6522445.png)
# For Loop
```
Marks=[90,94,87,81,85]
for marks in Marks:
    print('Marks'+ " " + str(marks))
```
![image](https://user-images.githubusercontent.com/111038642/188468688-d5d56351-a45f-4fa9-9d72-b2f09baf8b72.png)
# Range Function
```
for i in range(0,12,2):
    print(i)
```
![image](https://user-images.githubusercontent.com/111038642/188469133-16202f36-4524-4a50-83c7-183a6fe77861.png)
# Tuple
* Tuples are used to store multiple items in a single variable.
* A tuple is a collection which is ordered and unchangeable.
* Tuple items are ordered, unchangeable, and allow duplicate values.
```
number=(1,2,3,4)
print(type(number))
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```
![image](https://user-images.githubusercontent.com/111038642/188470272-0ed18b2c-5cdc-4c43-ac4d-804a54adafea.png)



