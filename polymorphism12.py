# Printer Polymorphism
class HP:
    def print_doc(self):
        print("Printing from HP")

class Canon:
    def print_doc(self):
        print("Printing from Canon")

def print_file(printer):
    printer.print_doc()

print_file(HP())
print_file(Canon())
