favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll = ['alice', 'mike', 'phil', 'sarah', 'dan']

for name in poll:
    if name in favorite_languages.keys():
        print('Thanks for responding ' + name + '.')
    else:
        print(name  + ' we invite you to take the poll for favorite language.')
