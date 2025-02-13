#MAXIMIZING XOR

status =True
while status:
    print("constarint : 1<=L<=R<=1000")
    L=int(input("enter first number\t"))
    R=int(input("enter second number\t"))
    if 1<=L and L<=R and R<=10**3:
        max=0
        for i in range(L,R+1):
            for j in range(L,R+1):
                if i^j>max:
                    max=i^j
        print("result:\t",max)
        status=False 
    else:
        print("follow the costarint")       
print("thankyou...")