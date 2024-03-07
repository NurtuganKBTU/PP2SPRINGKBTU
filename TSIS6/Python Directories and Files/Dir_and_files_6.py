# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
import os

for i in range(65, 90 + 1):
    file = open(f'C:/Users/acer/OneDrive/Рабочий стол/Everything/2nd Semester/PP2/LAB1/TSIS4/Generator/{chr(i)}.txt', 'x')
file.close()