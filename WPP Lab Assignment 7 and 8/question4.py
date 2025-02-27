class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __add__(self,second):
        return(self.salary+second.salary)
    def __sub__(self,second):
        return(self.salary-second.salary)    
          

name=input("enter the name of 1st employee:\t")
salary=int(input("enter salary of 1st employee:\t"))
first=Employee(name,salary)
name=input("enter the name of 2nd employee:\t")
salary=int(input("enter salary of 2nd employee:\t"))
second=Employee(name,salary)

combine=first+second
print("combined salary is",combine)
difference=first-second
print("difference of salary is",difference)

print("thankyou...")        
             