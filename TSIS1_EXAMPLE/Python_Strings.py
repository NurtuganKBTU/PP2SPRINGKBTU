# Python Strings

# Strings
"""Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello"."""
#1 You can display a string literal with the print() function:
print("Hello")
print('Hello')

#Assign String to a Variable
#2 Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
a = "Hello"
print(a)

#Multiline Strings
#3 You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
#4 Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

#Looping Through a String
#5 Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#String Length
#6 The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#Check String
#7 Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if NOT
#8 To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

#print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# ----------------------------------------------------------------------------------------------------------------
  
# Slicing Strings
#1 Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

#2 Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])

#3 Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])

# 4 
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])

# ---------------------------------------------------------------------------------------------------------------------

# Modify Strings
#1 The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#2 The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#3 The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#4 The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#5 The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# --------------------------------------------------------------------------------------------------------------------------

#String Concatenation
#1 Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

#2 To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# -------------------------------------------------------------------------------------------------------------------------

#Format - Strings

"""As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

ge = 36
txt = "My name is John, I am " + age
print(txt)

But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:"""

#1 Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#2 The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#3 You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Escape Characters
"""To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "We are the so-called "Vikings" from the north."

To fix this problem, use the escape character \":
"""

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

# \'	Single Quote:
txt = 'It\'s alright.'
print(txt) 

# \\	Backslash:
txt = "This will insert one \\ (backslash)."
print(txt) 

# \n	New Line:
txt = "Hello\nWorld!"
print(txt) 

# \r	Carriage Return
txt = "Hello\rWorld!"
print(txt) 

# \t	Tab
txt = "Hello\tWorld!"
print(txt) 

# \b	Backspace
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

# \ooo	Octal value
txt = "\110\145\154\154\157"
print(txt) 

# \xhh	Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# ---------------------------------------------------------------------------------------------------------------------------------------------

#String Methods

"""Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning"""


