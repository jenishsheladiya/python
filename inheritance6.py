
# Multiple inheritance
class Father:
    def show_family_role(self):
        print("father")

class Mother: 
    def show_family_show(self):
        print("mother")

class Child(Father, Mother):
    def show_child_role(self):
        print("child")

c = Child()
c.show_family_role()
c.show_child_role()