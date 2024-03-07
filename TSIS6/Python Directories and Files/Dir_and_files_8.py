# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

path = r'delfile.txt'
if os.path.exists(path):
   os.remove(path)
   print('removed')
else:
   print('your file does not exists')