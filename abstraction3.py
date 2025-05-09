
# Vehicle Example
from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def start_engine():
        pass

class Car():
    def start_engine(self):
        print("Car is start....")

class Bike():
    def start_engine(self):
        print("Bike is start....")

c1 = Car()
b1 = Bike()
c1.start_engine()
b1.start_engine()
