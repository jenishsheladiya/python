
# Method Overriding
class Shape:
    def area():
        return 0
    
class Circle(Shape):
    def __init__ (self, circle):
        self.circle = circle
    
    def area(self):
        return 3.14 * self.circle ** 2

class Rectangle(Circle):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

c = Circle(5)
r = Rectangle(4, 6)  
print(c.area())
print(r.area())
