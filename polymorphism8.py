#  Duck Typing Example
class Laptop:
    def execute(self):
        print("Running code in PyCharm")

class Mobile:
    def execute(self):
        print("Running code in VSCode")

def run(device):
    device.execute()

run(Laptop())
run(Mobile())
