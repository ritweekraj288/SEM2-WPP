#LOVE LETTER MYSTERY

testcase=int(input("enter the number of testcases between 1 to 10\t"))#testcase
stringList=[]#to store strings
if testcase>=1 and testcase<=10:#checking testcase constraints
    for i in range(testcase):#string input from user
        string=input("enter the string\t")
        if len(string)>=1 and len(string)<=10**4:#string constraint
            stringList.append(string)    
        else:
            print("restart the code and do remember the constraint")
            break
    for a in stringList:#operating each string
        i=list(a)
        count=0
        length=len(i)
        start=0#head
        end=length-1#tail
        while start!=end and not start>end:
            if i[start]!=i[end]:
                if i[start]<i[end]:
                    while i[start]!=i[end]:
                        i[end]=chr(ord(i[end])-1)
                        count+=1
                else:
                    while i[start]!=i[end]:
                        i[end]=chr(ord(i[end])+1)
                        count+=1
            start+=1#updation
            end-=1                 
        print(count)#printing final result                           
else:
    print("restart the code and do keep constraints in mind")