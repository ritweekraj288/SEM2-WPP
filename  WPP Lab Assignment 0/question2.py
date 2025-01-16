#PRINTING FACTORIAL OF THE ENTERED NUMBER

num=int(input("enter the number of which you want to calculate the factorial"))
fac=1

#CALCULATING FACTORIAL USING FOR

for i in range (1,num+1):
    fac*=i

#PRINTING THE FINAL RESULT

print("factorial of",num,"is",fac)
