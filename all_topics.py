# #conditional statment

# A = 2
# B = 3

# if(A>B):
#     print("A is greater than B")
# elif(A<B):
#     print("A is less than B")
# else:
#     print("..")

# """output : "A is less than B" """



# # list and tuple

# list = [1, 2, 3, 4, 5, 6]
# print(list[1:3])
# """output : [2,3]"""
# tuple = (1, 2, 3, 4, 5, 6)
# print(tuple[2:5])
# """output : (3, 4, 5)"""

# # dictionary and set

# dict ={
#     "name" : "james",
#     "age"  : "20"
# }
# print(len(dict))
# """outut : 2"""
# set = {1, 2, 3, 4, 5, 6}
# set.add(7)
# print(set)
# """output : {1, 2, 3, 4, 5, 6, 7}"""



# # while and for loop
# num = 1
# while num<=5:
#     print(num)
#     num +=1
# """output : 1 to 5 print numbers"""
# list = [1, 2, 3, 4, 5, 6]
# for i in list:
#     if(i == 2):
#         print("Found")
#     else:
#         print("searching..")
# """output : number 2 = found,  otherwise searching.."""        


# # functions and recursion

# def mul(a , b):
#     m = a * b
#     return m
# print(mul(2,3))
# """output: 6"""
# def show(n):
#     if(n == 2):
#         print("Found")    
#         return 
#     print(n)
#     show(n-1)
# show(5)
# """output : when recursion call 5 to infinite
#  number 2 stop and print Found"""

# # oop concepts
# # class and object
# class Names1:
#     name = "james"
# print(Names1.name)
# """output : james"""

# N1 = Names1()
# print(N1.name) 


# # constructor
# class Names2:
#     def __init__(self,name):
#         self.name = name

# N2 = Names2("james")
# print(N2.name)
# """output : james"""

# # static method

# class Names3:
#     @staticmethod
#     def name():
#         print("jenish")
# Names3.name()       
# """output:jenish
#    note:don't use parameters"""
