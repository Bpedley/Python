class Animal(object):
     
    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super(Dog, self).__init__(name)
        self.breed = breed


class Cat(Animal):

    def __init__(self, name, breed):
        super(Cat, self).__init__(name)
        self.breed = breed


class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):

    def __init__(self, name, salary=120000):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    
    def __init__(self, length):
        self.length = length


class Salmon(Fish):
    
    def __init__(self, length):
        super(Salmon, self).__init__(length)
        self.type_of_fish = 'Salmon'


class Halibut(Fish):

    def __init__(self, length):
        super(Halibut, self).__init__(length)
        self.type_of_fish = 'Halbiut'



rover = Dog('Rover', 'Bulldog')
satan = Cat('Satan', 'British')
mary = Person('Mary')
mary.pet = satan
frank = Employee('Frank', 120000)
frank.pet = rover
flipper = Fish(14)
crouse = Salmon(20)
harry = Halibut(16)
