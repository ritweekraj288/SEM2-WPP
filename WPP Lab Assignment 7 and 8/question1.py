class LinkedList:
    def __init__(self):
        print("initializing linked list...")
        self.LnkedLst=list()
        self.index=0
    def insert(self,element,position):
        self.LnkedLst.insert(position-1,element)
        self.index+=1
    def delete(self,position):
        if self.LnkedLst==[]:
            print("already empty...")
        else:
            print("deleted element is",self.LnkedLst.pop(position-1))
            self.index-=1
    def display(self):
        if self.LnkedLst==[]:
            print("empty list...")
        else:
            print("elements of linked list are:")
            for i in range(self.index):
                print(self.LnkedLst[i])
                             
S=LinkedList()
choice=1
while choice!=0:
    print("1 to insert")
    print("2 to delete")
    print("3 to display")
    print("0 to exit") 
    choice=int(input("enter your choice:\t")) 
    if choice==1:
        element=input("enter element to be inserted:\t")
        position=int(input("enter the position where to be inserted:\t"))
        S.insert(element,position)
    elif choice==2:
        position=int(input("enter the position from where to delete:\t"))
        S.delete(position)
    elif choice==3:
        S.display()                                   
print("thankyou...")    