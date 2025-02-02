#UTOPIAN TREE HEIGHT

t=int(input("enter the testcases between 1 to 10\t"))#testcases
if t>=1 and t<=10:
    cycle=list()
    for i in range(t):
        n=int(input("enter the number of cycles between 0 to 60\t"))#cycles
        if n>=0 and n<=60:
            cycle.append(n)
        else:
            print("restart the code and enter the values according to constarints")
            break 
    else:    
        for i in cycle:
            ht=1#initial height
            for j in range(1,i+1):
                if j%2==0:
                    ht=ht+1
                else:
                    ht=ht*2
            print(ht)#final height            
else:
    print("restart the code and enter the values according to the constraints")