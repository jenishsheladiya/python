# ATM Machine
class ATM:
    def __init__(self):
        self.__pin = "0000"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN changed")
        else:
            print("Wrong PIN")

atm = ATM()
atm.change_pin("0000", "1234")
