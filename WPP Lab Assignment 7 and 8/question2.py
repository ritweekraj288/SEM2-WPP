class Queue:
    def __init__(self):
        print("initialising queue...")
        self.q=list()
        self.count=0
    def enqueue(self,element):
        self.q.insert(0,element)  
        self.count+=1
    def dequeue(self):
        if self.count==0:
            print("already empty...")
        else:
            print("deleted element is",self.q.pop(-1))
            self.count-=1
    def display(self):
        if self.count==0:
            print('empty queue...')
        else:
            print("elemets of the queue are:\t")
            for i in range(self.count):
                print(self.q[i])    
        
S=Queue()
choice=1
while choice!=0:
    print("1 to enqueue")
    print("2 to dequeue")
    print("3 to diaplay")
    print("0 to exit")
    choice=int(input("enter your choice:\t"))
    if choice==1:
        element=input("enter the element:\t")
        S.enqueue(element)
    elif choice==2:
        S.dequeue()
    elif choice==3:
        S.display()        
print("thankyou...")        