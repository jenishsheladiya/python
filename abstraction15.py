# Transport Abstraction
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

class Bus(Transport):
    def move(self):
        print("Bus is moving on road.")

class Train(Transport):
    def move(self):
        print("Train is moving on track.")

t = Bus()
t.move()
