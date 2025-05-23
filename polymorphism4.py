
# Polymorphic Function
class Dog:
    def sound(self):
        return "Bark"
    
class Cow:
    def sound(self):
        return "Moo"
    
def describe(animal):
    print(animal.sound())

d = Dog()
c = Cow()
describe(d)
describe(c)