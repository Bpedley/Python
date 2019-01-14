current_users = ['anc', 'abc', 'aaa', 'ddd', 'eee']
new_users = ['abc', 'bbb', 'ccc', 'anc', 'anc']

for new_user in new_users:
    if new_user in current_users:
        print('Sorry, ' + new_user + ' you need to enter a new username.')
    else:
        print('Username ' + new_user + ' is available.')