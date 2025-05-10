# create a class of 3 subject and print the average with constructor
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def avg_sub(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"hi {self.name}your score is:{sum/3}")

s1 = student("jenish" , [99,98,97])
s1.avg_sub()
