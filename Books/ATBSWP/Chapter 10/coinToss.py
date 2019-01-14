import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

str_toss = ['heads', 'tails']
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess not in ('heads', 'tails'):
        raise Exception('You must guess "heads" or "tails".')
    logging.debug('The user\'s guess is: ' + guess)
toss = random.choice(str_toss) # 0 is tails, 1 is heads
logging.debug('The toss is: ' + str(toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if guess not in ('heads', 'tails'):
        raise Exception('You must guess "heads" or "tails".')
    logging.debug('The user\'s guess is: ' + guess)
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program')
