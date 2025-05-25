
# Multiple inheritance
class A:
    VarA = ("Welcome to class A")

class B:
    VarB = ("Welcome to class B")

class C(A, B):
    VarC = ("Welcome to class C")

c1 = C()
print(c1.VarA)
print(c1.VarB)
print(c1.VarC)