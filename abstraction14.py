# Shape Drawing System
from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Line(Drawable):
    def draw(self):
        print("Drawing a line")

class Circle(Drawable):
    def draw(self):
        print("Drawing a circle")

shape = Line()
shape.draw()
