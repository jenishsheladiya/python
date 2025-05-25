# Animal Sound Example
class Lion:
    def speak(self):
        print("Roar")

class Snake:
    def speak(self):
        print("Hiss")

animals = [Lion(), Snake()]
for a in animals:
    a.speak()
