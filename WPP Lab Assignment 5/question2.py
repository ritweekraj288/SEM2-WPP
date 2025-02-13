#HALLOWEEN PARTY

status1=True
while status1:
    print("constraint : 1<=T<=10")
    T=int(input("enter number of testcases:\t"))
    if 1<=T and T<=10:
        status2=True
        cuts=list()
        while status2:
            count=0
            while count!=T:
                print("constraint : 2<=K<=10^7")
                K=int(input("enter number of cuts\t"))
                if 2<=K and K<=10**7:
                    cuts.append(K)
                    count+=1
                else:
                    print("follow the constraint") 
            status2=False 
        for i in cuts:
            if i%2==0:
                print((i//2)*(i//2))      
            else:
                print((i//2)*((i//2)+1))              
        status1=False           
    else:
        print("follow the constraint")            