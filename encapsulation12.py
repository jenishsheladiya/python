# Phone Contact List
class ContactList:
    def __init__(self):
        self.__contacts = {}

    def add_contact(self, name, number):
        self.__contacts[name] = number

    def get_number(self, name):
        return self.__contacts.get(name, "Not found")

cl = ContactList()
cl.add_contact("Amit", "9999999999")
print(cl.get_number("Amit"))
