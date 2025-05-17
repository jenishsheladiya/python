# Password Manager
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

u = User("admin", "1234")
print(u.check_password("1234"))  # Output: True
