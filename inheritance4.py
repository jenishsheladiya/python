
# Basic inheritance
class Animal:
    def speak():
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

a1 = Dog()
a1.speak()