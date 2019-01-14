print("Enter 'q' at any time to quit.\n")

while True:
    try:
        num_1 = input('Enter first number: ')
        if num_1 == 'q':
            break
        
        num_1 = int(num_1)  

        num_2 = input('Enter second number: ')
        if num_2 == 'q':
            break

        num_2 = int(num_2)
        
    except ValueError:
        print('Error, not a numbers.')

    else:
        sum = num_1 + num_2
        print(sum)