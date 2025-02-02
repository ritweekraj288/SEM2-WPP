#DIGITAL ROOT OF A NUMBER USING FUNCTION

#FUNCTION

def DigitalRoot(a):
    sum=a
    temp=a
    while sum>9:
        sum=0
        while temp!=0:
            rem=temp%10
            temp//=10
            sum+=rem
        temp=sum    
    print("value of digital root of",a,"is",sum)

#MAIN FUNCTION

num=int(input("enter a positive number\t"))
if num<0:
    print("restart the code and enter a positive number")
else:
    DigitalRoot(num)    