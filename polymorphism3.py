
# Operator Overloading
class Box:
    def __init__(self, volume):
        self.volume = volume

    def __add__(self, volume2):
        return self.volume + volume2.volume
    
b1 = Box(20)
b2 = Box(30)
print(b1 + b2)