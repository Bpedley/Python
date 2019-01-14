import json

number = input('Enter a favorite number: ')

filename = 'fav.json'
with open(filename, 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.")