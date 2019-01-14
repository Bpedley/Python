# переменная обозначающая кол-во типов людей
types_of_people = 10
# выводит на экран текст с значением переменной выше
x = f"There are {types_of_people} types of people."

# объявление переменных с значением типа string
binary = "binary"
do_not = "don't"
# вывод на экран текста с значением переменных выше
y = f"Those who know {binary} and those who {do_not}."

# вывод на экран строк
print(x)
print(y)

# вывод на экран тех же строк, но с добавлением в начале текста
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False # объявление переменной со значением False
# объявление переменной типа string
joke_evaluation = "Isn't that joke so funny?! {}"

# выводит на экран текста из joke_evaluation и значения переменной hilarious
print(joke_evaluation.format(hilarious))

# объявление 2 переменных типа string
w = "This is the left side of..."
e = "a string with a right side."

print(w + e) # вывод на экран значений 2 переменных выше
