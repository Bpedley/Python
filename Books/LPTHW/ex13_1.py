from sys import argv
script, number_1, number_2 = argv

operator = input("Введите оператор: ")
print("The script is called:", script)
print("The first number is:", number_1)
print("The second number is:", number_2)

try:
    if operator == "+":
        print("Answer is:", int(number_1) + int(number_2))
    elif operator == "-":
        print("Answer is:", int(number_1) - int(number_2))
    elif operator == "*":
        print("Answer is:", int(number_1) * int(number_2))
    elif operator == "/":
        print("Answer is:", int(number_1) / int(number_2))
    else:
        print("Wrong operator")
except ZeroDivisionError:
    print("Деление на ноль невозможно!")
