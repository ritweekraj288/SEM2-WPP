# 100 RANDOM INTEGERS WITH ONLY 0 OR 1

# IMPORTING MODULE

import random

lst=[] #empty list 

# STORING 100 INTEGERS IN LIST 

while len(lst)!=100:
    status=1 #status used whie checking the number
    it=random.randint(1,1000000) #generating random integers
    num=it 
    
    #CHECKING FOR THE NUMBER

    while num!=0 :
        rem=num%10
        num//=10
        if rem==0 or rem==1:
            pass
        else:
            status=0

    if status==1:
        lst.append(it)    
    
#PRINTING LIST

print(lst)

#CALCULATING LARGEST NUMBER OF ZEROES IN A ROW

count=0 # counting number of zeroes
cmax=0 # maximum number of zeroes
elmt=0 # element with maximum zero
for i in lst:
    store=i # to save the value of i
    
    #CREARTING LIST OF THIS ELEMENT TO PERFORM THE TASK

    s=str(i) #converting to string
    l=list(s) #converting to list
    
    temp=0
    tempmax=0
    for j in l:
        if j=='0':
            count+=1
            temp=count
        else:
            temp=count
            count=0
        if temp>tempmax:
            tempmax=temp        
        
    count=tempmax
    if count>cmax:
        cmax=count
        elmt=store
    
    count=0
#PRINTING FINAL RESULT

print("element with maximum number of zeros is",elmt,"with",cmax,"number of zeroes")