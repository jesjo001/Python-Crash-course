

class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'my name is {self.name} i am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extend Class

class Customer(User):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_ballance(self, balance):
        self.ballance = balance

    def greeting(self):
        return f'my name is {self.name} i am {self.age} and my balance is {self.balance}'



brad = User('Jesjo ', "jesjo@yahoo.com", 30)
James = Customer('Jesjo ', "jesjo@yahoo.com", 30)

print(brad.name)
print(James.name)
print(James.greeting())
