# Bird Example
class Parrot:
    def fly(self):
        print("Parrot can fly")

class Penguin:
    def fly(self):
        print("Penguin can't fly")

for bird in (Parrot(), Penguin()):
    bird.fly()
