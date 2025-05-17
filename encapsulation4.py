# Car Speed Control
class Car:
    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed += 10

    def get_speed(self):
        return self.__speed

c = Car()
c.accelerate()
print(c.get_speed())  # Output: 10
