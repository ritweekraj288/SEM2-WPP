#PRINTING NUMBER OF POSITIONS WHERE DIGITS EXACTLY DIVIDE THE NUMBER

t=int(input("enter the number of testcases between 1 to 15\t"))#testcases

#CONSTRAINT FOR TESTCASE

if t>=1 and t<=15:
    for i in range(t):
        num=int(input("enter the number between 0 to 10^10\t"))#number
        if num>=0&num<=10**10:
            store=num#to store the number
            count=0#to count the digits
            while num!=0:
                rem=num%10#remainder
                num//=10#updation

                #CHECKING
                
                if store%rem==0:
                    count+=1  
            
            #PRINTING RESULT

            print(store,"is divisible by",count,"of its digits")

        else:
            print("restart the code keeping the constraint in mind")
            break

else:
    print("restart the code keeping the constraint in mind")


 

