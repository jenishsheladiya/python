#  Login System
class Admin:
    def login(self):
        print("Admin login")

class User:
    def login(self):
        print("User login")

def system_login(role):
    role.login()

system_login(Admin())
system_login(User())
