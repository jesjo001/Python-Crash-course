# A function is a block of code which only runs when it is called. In Python, we do not use curly brackets, we use indentation with tabs or spaces


# create a functions

def sayHello(name='Samuel'):
    print(f'Hello {name}')


sayHello('Mathew')
sayHello()

def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(2, 8))


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, and 
# can only have one expression. very simmillar to JS arrow function

getNewSum = lambda num1, num2: num1 + num2;

print(getNewSum(9, 5))