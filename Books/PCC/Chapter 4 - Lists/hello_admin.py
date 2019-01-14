names = ['Adam', 'Eva', 'Admin', 'Mike']

if names == []:
    print('We need to find some users!')
else:
    for name in names:
        if name == 'Admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + name + ', thank you for logging in again.')
