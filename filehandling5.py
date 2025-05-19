
# create a syntex replace data
with open("sample.txt", "r") as f:
    data = f.read()

newdata = data.replace("Java", "Python")
print(newdata)

with open("sample.txt", "w")as f:
    f.write(newdata)