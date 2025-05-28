# Animal Sounds (Polymorphic Inheritance)
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]
for a in animals:
    a.speak()
