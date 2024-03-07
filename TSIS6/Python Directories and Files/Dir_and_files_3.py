# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

path = r'C:\Users\acer\OneDrive\Рабочий стол\Everything\2nd Semester\PP2\LAB1\TSIS4'
if os.path.exists(path):
   print("Yes")
   filename = os.path.split(path)
   print(filename)
   print(filename[0])
   print(filename[1])
else:
   print("path is not exist")