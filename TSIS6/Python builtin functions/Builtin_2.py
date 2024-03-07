# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def RealMadrid(s):
   upperletters = 0
   lowerletters = 0
   for i in s:
      if i.islower():
         lowerletters += 1
      if i.isupper():
         upperletters += 1
   return f"{upperletters}\n{lowerletters}" 
s = input()

print(RealMadrid(s))