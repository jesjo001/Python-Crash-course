import json

# Sample JSON

userJson = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dictionary
user = json.loads(userJson)

print(user)
print(user['first_name'])

print(user)
print(user['first_name'])

car = { 'make': 'ford', 'model': 'mustang', 'year': 2022}

carJson = json.dumps(car)
print(carJson)