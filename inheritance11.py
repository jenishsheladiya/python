#  Employee Hierarchy (Multi-level Inheritance)
class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def work(self):
        print(f"{self.name} is writing code.")

class TeamLead(Developer):
    def manage(self):
        print(f"{self.name} is managing a team.")

lead = TeamLead("Ravi")
lead.work()
lead.manage()
