#BIGGER IS GREATER

status1=True
while status1:
    print("constraint : 1<=t<=10^5")
    t=int(input("enter number of testcases\t"))
    if 1<=t and t<=10**5:
        count=0
        word=list()
        while count!=t:
            print("constraint : 1<=|w|<=100")
            w=input("enter the word\t")
            if 1<=len(w) and len(w)<=100:
                count+=1
                word.append(w)
            else:
                print("follow the constraint")   
        for i in word:
            flag=1
            flag2=1
            for j in range(len(i)-1,-1,-1):
                for k in range(j-1,-1,-1):
                    if i[j]>i[k]:
                        lst=list(i)
                        lst[j],lst[k]=lst[k],lst[j]
                        store=str()
                        for a in range(len(lst)):
                            store+=lst[a]
                        print(store)
                        flag2=0
                        break
                    else:
                        flag=0
                if flag2==0:    
                    break        
            if flag==0:
                print("no answer")
        status1=False                    
    else:
        print("follow the constraint")


