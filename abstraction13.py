# Game Character Abilities
from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Warrior swings sword.")

class Mage(Character):
    def attack(self):
        print("Mage casts fireball.")

player = Mage()
player.attack()
