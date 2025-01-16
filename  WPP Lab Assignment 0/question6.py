# PRINTING REVERSE OF THE ENTERED NUMBER

num=int(input("enter the numebr whose reverse you want to be printed"))

store=num  #TO STORE THE ORIGINAL VALUE OF NUM

#CALCULATING REVERSE OF THE ENTERED NUMBER

rev=0
while num>0:
    rem=num%10  #REMAINDER
    num=num//10
    rev=(10*rev)+rem  #REVERSE

#PRINTING REVERSE OF THE ENTERED NUMBER

print("reverse of the number",store,"is",rev)
