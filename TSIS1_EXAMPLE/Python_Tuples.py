mytuple = ("apple", "banana", "cherry")

#Tuple
"""Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets."""

#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple Items
"""Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc."""

#Ordered
"""When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
"""

#Unchangeable
"""Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created."""

#Allow Duplicates
#1 Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple Length

#2 Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Create Tuple With One Item
#3 One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple Items - Data Types
#4 String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#5 A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")

# type()
#6 What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() Constructor
#7 Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Access Tuple Items

# Access Tuple Items
#1 Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

"""Note: The first item has index 0."""

#Negative Indexing
"""Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc."""

#2 Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
"""You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items."""

#3 Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

"""Note: The search will start at index 2 (included) and end at index 5 (not included)."""

#4 This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#5 This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

#Range of Negative Indexes
#6 This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Check if Item Exists
#7 Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Update Tuples

#Change Tuple Values
"""Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple."""

#1 Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#Add Items
"""Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple."""

#2 Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

"""2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:"""

#3 Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

"""Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple."""

#Remove Items
"""Note: You cannot remove items in a tuple."""

#4 Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#