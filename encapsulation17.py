# Temperature Controller
class Thermostat:
    def __init__(self):
        self.__temperature = 22

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp

    def get_temperature(self):
        return self.__temperature

t = Thermostat()
t.set_temperature(25)
print(t.get_temperature())
