# Shape Area Calculation
class Rectangle:
    def area(self):
        print("Area = w * h")

class Circle:
    def area(self):
        print("Area = π * r^2")

for shape in (Rectangle(), Circle()):
    shape.area()
