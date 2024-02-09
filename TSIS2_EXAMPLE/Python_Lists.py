#Python Lists
mylist = ["apple", "banana", "cherry"]

#1 Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

#List Items

"""List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc."""

#Ordered

"""When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the items will not change."""

# Changeable

#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#2 Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3 To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#4 List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#5 A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

#6 <class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#7 Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Python Collections (Arrays)

"""There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

"""

# ------------------------------------------------------------------------------------------------------------------------------------------------------

#Access List Items

#1 Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Note: The first item has index 0.
""" Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc. """

#2 Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#3 Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).

#4 This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#5 This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#6 This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

"""To determine if a specified item is present in a list use the in keyword:"""

#7 Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# ------------------------------------------------------------------------------------------------------------------------------------------------------

#Change List Items
  
# Change Item Value
#1 Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
#2 Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#3 Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

"""Note: The length of the list will change when the number of items inserted does not match the number of items replaced."""

#4 Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert Items

"""To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:"""

#5 Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

"""Note: As a result of the example above, the list will now contain 4 items."""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Add List Items

#Append Items
#1 Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert Items
#2 Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

"""Note: As a result of the examples above, the lists will now contain 4 items."""

#Extend List
#3 Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable
#4 Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Remove List Items

#Remove Specified Item
#1 Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#2 Remove the first occurance of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#3 Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#4 Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#5 Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#6 Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
"""The clear() method empties the list.

The list still remains, but it has no content."""

#7 Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Loop List

# Loop Through a List
#1 Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

"""You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable."""

#2 Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

"""The iterable created in the example above is [0, 1, 2]."""

#Using a While Loop

"""You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

Remember to increase the index by 1 after each iteration."""

#3 Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension

#4 A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# List Comprehension

#List Comprehension

"""List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:"""

#1 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#2 With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#The Syntax
newlist = [expression for item in iterable if condition == True]
"""The return value is a new list, leaving the old list unchanged."""

#Condition
#3 Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

"""The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

The condition is optional and can be omitted:"""

#4 With no if statement:
newlist = [x for x in fruits]

#Iterable
#5 You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

#6 Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

#Expression

#7 Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

#8 Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

#9 Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Sort Lists

#Sort List Alphanumerically

#1 List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#2 Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#Sort Descending
#3 To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#4 Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function

"""You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):"""

#5 Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort
#6 By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#7 Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
"""What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements."""

#8 Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Copy Lists

# Copy a List
"""You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy()."""

#1 Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#2 Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# Join Lists

#Join Two Lists
"""There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator."""

#1 Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#2 Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#3 Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------

# List Methods

"""Method	    Description
append()	   Adds an element at the end of the list
clear()	     Removes all the elements from the list
copy()	     Returns a copy of the list
count()	     Returns the number of elements with the specified value
extend()	   Add the elements of a list (or any iterable), to the end of the current list
index()	     Returns the index of the first element with the specified value
insert()	   Adds an element at the specified position
pop()	       Removes the element at the specified position
remove()	   Removes the item with the specified value
reverse()	   Reverses the order of the list
sort()	     Sorts the list
"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
