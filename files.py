

# Opena file
myFile = open('myfile.txt', 'w')

# Get some information about
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to files
myFile.write("I love Python")
myFile.write("and Javascript")
myFile.close()


# Append to files
myFile = open('myFile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()


# Read from a files
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
