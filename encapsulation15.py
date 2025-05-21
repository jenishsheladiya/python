# Secure Door Access
class Door:
    def __init__(self):
        self.__is_locked = True

    def unlock(self, code):
        if code == "1234":
            self.__is_locked = False

    def is_open(self):
        return not self.__is_locked

d = Door()
d.unlock("1234")
print(d.is_open())
