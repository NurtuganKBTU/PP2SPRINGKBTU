# Write a Python program to count the number of lines in a text file.
file = open('akatsuki.txt', 'r')

count = 0
for i in file:
    if i != '\n':
        count += 1
print(count)