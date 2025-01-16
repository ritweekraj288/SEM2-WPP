#CODEDOCS ADMIN PSYCHO

memb=int(input("enter the number of members in the party"))

#CREATING A LIST TO CONTAIN ALL THE HEIGHTS OF MEMBERS

list=[]
for h in range (memb):
    ht=int(input("enter the height of the member"))
    list.append(ht)
print("height of the members arranged randomly in queue are")
for i in list:
    print(i,end='     ')

#PERFORMING THE SWAPPING TASK

swap=0
index=0

for a in range(memb):
    min=list[a]
    for b in range(a,memb):
        if min>list[b]:
            min=list[b]
            index=b
            

    if min!=list[a]:
        swap+=1
        extra=list[a]
        list[a]=min
        list[index]=extra

#PRINTING FINAL RESULT    
print("\ntotal swaps performed is swap",swap)
print("AFTER SWAPPING")
print("heights in ascending order are")
for i in list:
    print(i,end='     ')
print("\n")


