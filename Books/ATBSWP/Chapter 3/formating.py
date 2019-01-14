input_str = input('Введите имя: ')
ch = int(input('Введите колво знаков в строке: '))

if (ch - len(input_str)) % 2 == 0:
    print(('{0:*^'+str(ch)+'}').format(input_str))
else:
    ch += 1
    print(('{0:*^'+str(ch)+'}').format(input_str))
