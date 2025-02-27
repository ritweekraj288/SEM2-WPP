class Shape:
    def __init__(self):
        print("starting the program...")
    def intro(self):
        print("intitializing the task of perimeter and area calculation...")
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def perimeter(self):
        print("perimeter of the rectangle is",2*(self.length+self.breadth)) 
    def area(self):
        print("area of the rectangle is",self.length*self.breadth) 
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius  
    def perimeter(self):
        print("perimeter of the circle is",2*3.14*self.radius)
    def area(self):
        print("area of the circle is",3.14*self.radius*self.radius)            

S=Shape()
choice=1
while choice!=0:
    print("1 for rectangle")
    print("2 for circle")
    print("0 to exit")
    choice=int(input("enter your choice:\t"))
    if choice==1:
        length=int(input("enter length:\t"))
        breadth=int(input("enter breadth:\t"))
        R=Rectangle(length,breadth)
        R.intro()#accessing parent class method from child class
        R.perimeter()
        R.area()
    elif choice==2:
        radius=int(input("enter radius of the circle:\t"))
        C=Circle(radius) 
        C.intro()#accessing parent class method from child class
        C.perimeter()
        C.area() 
print("thankyou...")          
        


        