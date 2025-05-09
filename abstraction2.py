
# area of a square 
class Shape:
    def area(self):
     side = int(input("Enter the side length: "))
     area = print(f"Area of the square: {side * side}")
     return area
    
s1 = Shape()
s1.area()