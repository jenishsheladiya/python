# Operator Overloading
class Point:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

p1 = Point(5)
p2 = Point(10)
print(p1 + p2)
