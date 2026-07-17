from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, "Cat")

    def make_sound(self):
        print('meow')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "Dog")

    def make_sound(self):
        print('woof-woof')


class Chicken(Animal):
    def __init__(self):
        Animal.__init__(self, "Chicken")

    def make_sound(self):
        print('chick-chick')


class Duck(Animal):
    def __init__(self):
        Animal.__init__(self, "Duck")

    def make_sound(self):
        print('quack-quack')


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()


animals = [Cat(), Dog(), Chicken(), Duck()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
