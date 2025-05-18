# simple file handling
f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
data = f.read()
print(data)
f.close()
