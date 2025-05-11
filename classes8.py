
# inheritance - animal and dog class
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof Woof")

d1 = Dog()
d1.speak()    
