# Write a Python program to copy the contents of a file to another file
file1 = open('akatsuki.txt', 'r')
file2 = open('hokage.txt', 'w')

for i in file1:
    file2.write(str(i))
file1.close()
file2.close()

file2 = open('hokage.txt', 'r')
print(file2.read())