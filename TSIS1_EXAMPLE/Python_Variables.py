# Python Variables

#1
x = 5
y = "John"
print(x)
print(y)

# 2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#4
x = 5
y = "John"
print(type(x))
print(type(y))

#5
x = "John"
# is the same as
x = 'John'

#6
a = 4
A = "Sally"
#A will not overwrite a

# ------------------------------------------------

# Variable Names

#1  Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#2  Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"


# Multi Words Variable Names


# Camel Case.. Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case.. Each word starts with a capital letter:
MyVariableName = "John"


# Snake Case.. Each word is separated by an underscore character:
my_variable_name = "John"

# ------------------------------------------------

# Assign Multiple Values

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# ------------------------------------------------

# Output Variables

#1 The Python print() function is often used to output variables.
x = "Python is awesome"
print(x)

#2 In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#3 You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#4 For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#5 In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
print(x + y)

#6 The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)

# ------------------------------------------------

# Global Variables

#1 Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#2 Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#3 If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#4 To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
