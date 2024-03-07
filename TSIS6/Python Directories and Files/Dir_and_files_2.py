# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
import os

path = r'C:\Users\acer\OneDrive\Рабочий стол\Everything\2nd Semester\PP2\LAB1\TSIS4'
if os.path.exists(path):
    print("this file exists")
if os.access(path, os.R_OK):
    print("file is readable")
if os.access(path, os.W_OK):
    print("file is writeable")
if os.access(path, os.X_OK):
    print("file is executable")