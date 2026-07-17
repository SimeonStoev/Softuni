import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.radius * self.radius * math.pi, 2)


class AreaCalculator:

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Circle(2), Circle(3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
