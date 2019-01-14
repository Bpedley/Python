'''
pizza = ''
while pizza != 'quit':
    pizza = input('Enter a tapping or "quit" when you are finished: ')
    if pizza != 'quit':
        print('You add ' + pizza + ' tapping.')
'''

age = ''
while age != 'quit':
    age = input('Entar age or type "quit": ')
    if age == 'quit':
        break
    else:
        if 0 < int(age) < 3:
            print('Ticket is free!')
        elif 3 <= int(age) <= 12:
            print('Ticket is 10$')
        elif int(age) > 12:
            print('Ticket is 15$')