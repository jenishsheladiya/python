#  Password guessing with limited tries
password = "secret"
attempt = ""
tries = 0

while attempt != password and tries < 3:
    attempt = input("Enter password: ")
    tries += 1

if attempt == password:
    print("Access granted!")
else:
    print("Access denied!")
