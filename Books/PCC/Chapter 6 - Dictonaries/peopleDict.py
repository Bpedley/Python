people = {
    'ae': {
        'first_name': 'Albert',
        'last_name': 'Einstein',
        'age': 67,
        'city': 'Princeton',
        },
    'mc': {
        'first_name': 'Marie',
        'last_name': 'Curie',
        'age': 19,
        'city': 'Paris',
        },
}

for username, user_info in people.items():
    print('\nUsername: ' + username)
    print('Full name: ' + user_info['first_name'] + ' ' + user_info['last_name'])
    print('Age: ' + str(user_info['age'])
    print('City: ' + user_info['city'])