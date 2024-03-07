# Write a Python program to write a list to a file.
file = open('akatsuki.txt', 'w')
mylist = ['"Nobody Cared Who I Was', 'Until I Put On The Mask"', 'Tobi']
for i in mylist:
    file.write(str(i) + '\n')
file.close()
f = open('akatsuki.txt', 'r')
print(f.read())