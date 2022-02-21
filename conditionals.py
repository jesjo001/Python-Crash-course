x = 10 
y = 10 

# if 
if x > y:
    print(f'{x} is greater than {y}')


# simple if else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')


# simple elif 

# elif
if x > y:
    print(f'{x} is greater than {y}')
elif y == x:
    print(f'{y} is equal to {x}')
else:
    print(f'{y} is greater than {x}')


# Nested if
if x > 2:
    if x <= 10:
        print(f'{x} is greater and less than 10')

if x > 2 and x <= 12:
    print(f'{x} is greater 2 and less than 10')

# or
if x > 2 or x <= 12:
    print(f'{x} is greater 2 or less than 12')

# not
if not( x == 12):
    print(f'{x} x is not equal to 12')


# Membership Operators (not, not in)
# Membership operators are used to test if a sequence is presented in an object

numbers = [ 1, 0, 2, 3, 4, 10];

if x in numbers:
    print(x in numbers) 

# Ideally Operators (is, is not) - 
# Compares the object not is they arre equal, 
# but if they are actually the same object, with the same memory location

# is
