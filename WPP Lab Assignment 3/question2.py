#IS FIBO(to find whether the number is in fibonacci series or not)

#FUNCTIONS

def IsFibo(n):#to find fibonacci element or not
    f=FiboList(n)
    if n in f:
        print("IsFibo")
    else:
        print("IsNotFibo")   

def PrintList(l):
    for i in l:
        print(i)  

def FiboList(n):
    f=[0,1]
    a,b=0,1
    c=1
    f.extend((a,b))
    while c<=n:
        c=a+b
        f.append(c)
        a=b
        b=c
    return f


#MAIN 

t=int(input("enter the number of test cases\t"))#test cases
numlist=list()#to store entries
for i in range(t):
    num=int(input("enter the element\t"))
    numlist.append(num)

PrintList(numlist)

for i in range(t):
    IsFibo(numlist[i])

