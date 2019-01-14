import json

filename = 'fav.json'
with open(filename) as f:
    number = json.load(f)

print('I know your favorite number! It’s ' + str(number) + '.')