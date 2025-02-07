#SHERLOCK AND SQUARES

testcase=int(input("enter number of testcases\t"))#testcase
if testcase>=1 and testcase<=100:#testcase constraint checking
    for i in range(testcase):#running according to number of testcases
        num1=int(input("enter a number\t"))
        num2=int(input("enter another number\t"))
        if num1>=1 and num2>=num1 and num2<=10**9:#numbers constraint
            count=0
            for i in range(num1,num2+1):
                if i**0.5%1==0:
                    count+=1
            print(count)#printing result
        else:
            print("restart the code and enter values according to constraints")
else:
    print("restart the code and enter values according to constraints")