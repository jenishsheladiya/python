# Online Shopping - Discount Strategy
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price

class PercentageDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price * 0.9

item = PercentageDiscount()
print(item.apply_discount(1000))
