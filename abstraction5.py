# Shape Area Calculator
from abc import ABC ,abstractmethod
import math
class Shape():
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
        return math.pi * self.radius ** 2

r1 = Rectangle(10,5)
print(r1.area())
c1 = Circle(7)
print(c1.area()) 