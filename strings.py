name = 'Brade'
age = 37

# concatenating
# we can only concatenate string so 
# youll need to convert any other type to string to concatenate it

print('Hello my name is ' + name )
print('Hello my name is ' + name + 'my age is ' + str(age))


# String formatting
# Atgument by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

#F-Strings
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# capitalize
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap case characters
print(s.swapcase())

# Get length of string
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

#  Starts with first
print(s.startswith('hello'))

# Ends with
print(s.endswith('world'))
print(s.endswith('d'))


# Split 
print(s.split())

# Find Position
print(s.find('d'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphanumeric
print(s.isalpha())

#  Is all numeric
print(s.isnumeric())