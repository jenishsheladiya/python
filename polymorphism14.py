# Greet Different Peo
class English:
    def greet(self):
        print("Hello!")

class Hindi:
    def greet(self):
        print("Namaste!")

for person in (English(), Hindi()):
    person.greet()
