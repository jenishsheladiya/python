# Game Characters (Method Overriding)
class Character:
    def attack(self):
        print("Basic attack")

class Warrior(Character):
    def attack(self):
        print("Sword slash!")

class Archer(Character):
    def attack(self):
        print("Arrow shot!")

w = Warrior()
a = Archer()
w.attack()
a.attack()
