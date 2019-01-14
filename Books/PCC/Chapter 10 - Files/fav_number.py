import json

filename = 'fav.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input('Enter a favorite number: ')
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Thanks! I'll remember that.")
else:
    print('I know your favorite number! It’s ' + str(number) + '.')