from re import compile

UP_REGEX = compile(r'[A-Z]')
LOW_REGEX = compile(r'[a-z]')
DIG_REGEX = compile(r'\d')

def check_password(text):
    return bool(UP_REGEX.search(text) and LOW_REGEX.search(text) and
                DIG_REGEX.search(text))

pas = input('Enter a password: ')
if check_password(pas) is True:
    print('Strong password')
else:
    print('Weak password')
