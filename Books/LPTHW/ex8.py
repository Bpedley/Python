formater = "{} {} {} {}" # шаблон форматирования для 4 аргументов

# вывод на экран 5 строчек с 4 аргументами, с использованием форматирования
print(formater.format(1, 2, 3, 4))
print(formater.format("one", "two", "three", "four"))
print(formater.format(True, False, False, True))
print(formater.format(formater, formater, formater, formater))
print(formater.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
