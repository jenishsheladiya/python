
# Multi-level inheritance
class Organism:
    def info(self):
        print("I am a Oraganism")

class Animal(Organism):
    def info(self):
        super().info()
        print("I am an Animal")
    
class Human(Animal):
    def info(self):
        super().info()
        print("I am  Human")

h = Human()
h.info()
