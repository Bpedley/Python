filename = 'guests.txt'

while True:
    name = input('Enter a name or q to exit: ')
    if name == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(name + '\n')
        print('Greetings, ' + name + '!')
        