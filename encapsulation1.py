#  Basic Encapsulation with Private Attribute
class Person:
    def __init__(self, name):
        self.__name = name  # private

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p1 = Person("Alice")
print(p1.get_name())  # Output: Alice
p1.set_name("Bob")
print(p1.get_name())  # Output: Bob
