import math
class Vector2D:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    def magnitude(self):
        return (self.x**2+self.y**2)**0.5
    def rotation(self):
        return (math.atan(self.y/self.x)) 
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5 
    def dotproduct(self,other):
        return (self.x*other.x+self.y*other.y)
    def crossproduct(self,other):
        return "not defined for 2D"
    
class Vector3D(Vector2D):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z
    def magnitude(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    def rotation(self):
        return (math.acos(self.x/self.magnitude())) 
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2+(self.y-other.y)**2)**0.5 
    def dotproduct(self,other):
        return (self.x*other.x+self.y*other.y+self.z*other.z)
    def crossproduct(self,other):
        return str(self.y*other.z-self.z*other.y)+"i + "+str(self.z*other.x-self.x*other.z) +"j + "+str(self.x*other.y-self.y*other.x)+"k"   

choice=1
while choice!=0:
    print("1 for 2D vectors")
    print("2 for 3D vectors")
    print("0 for exit")
    choice=int(input("enter your choice:\t"))
    if choice==1:
        print("enter details of vector 1")
        x=int(input("x coordinate:\t"))
        y=int(input("y coordinate:\t"))
        V1=Vector2D(x,y)
        print("magnitude:\t",V1.magnitude())
        print("rotation with x axis",V1.rotation())

        print("enter details of vector 2")
        x=int(input("x coordinate:\t"))
        y=int(input("y coordinate:\t"))
        V2=Vector2D(x,y)
        print("magnitude:\t",V2.magnitude())
        print("rotation with x axis",V2.rotation())

        print("distance between the two",V1.distance(V2))
        print("dotproduct between the two",V1.dotproduct(V2))
        print("crossproduct between the two",V1.crossproduct(V2))
    elif choice==2:
        print("enter details of vector 1")
        x=int(input("x coordinate:\t"))
        y=int(input("y coordinate:\t"))
        z=int(input("z coordinate:\t"))
        V1=Vector3D(x,y,z)
        print("magnitude:\t",V1.magnitude())
        print("rotation with x axis",V1.rotation())

        print("enter details of vector 2")
        x=int(input("x coordinate:\t"))
        y=int(input("y coordinate:\t"))
        z=int(input("z coordinate:\t"))
        V2=Vector3D(x,y,z)
        print("magnitude:\t",V2.magnitude())
        print("rotation with x axis",V2.rotation())

        print("distance between the two",V1.distance(V2))
        print("dotproduct between the two",V1.dotproduct(V2))
        print("crossproduct between the two",V1.crossproduct(V2))
print("thankyou...")    



        
        
      



