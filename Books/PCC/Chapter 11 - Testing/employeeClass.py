class Employee():

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, add=50000):
        self.salary += add

employee = Employee('Egor', 'Kuchin', 10000)
employee.give_raise()
print(employee.salary)
employee.give_raise(10000)
print(employee.salary)