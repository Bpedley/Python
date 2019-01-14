# объявляем переменные и присваиваем им значения
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
# объявляем переменные
# значения неоторых посчитается с помощью созданных раннее переменных
# и их значений
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


# выводим на экран текст и получившиеся значения
print("There are", cars, "cars avaliable.")
print("There are only", drivers, "drivers avaliable.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
