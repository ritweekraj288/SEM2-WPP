#EQUIVALENCE CLASS FOR MODULO 5

#CREATING EMPTY SETS TO CREATE VARIOUS EQUIVALENCE CLASSES

rem0=set()#to store numbers which give 0 as remainder on division with 5
rem1=set()#to store numbers which give 1 as remainder on division with 5
rem2=set()#to store numbers which give 2 as remainder on division with 5
rem3=set()#to store numbers which give 3 as remainder on division with 5
rem4=set()#to store numbers which give 4 as remainder on division with 5
original=set()#to store all th numbers from 1 to 10000

#STORING VALUES

for i in range(1,10001):

    #ORIGINAL SET

    original.add(i)

    #REMAINDER 1

    if i%5==0:
        rem0.add(i)
    elif i%5==1:
        rem1.add(i) 
    elif i%5==2:
        rem2.add(i) 
    elif i%5==3:
        rem3.add(i) 
    elif i%5==4:
        rem4.add(i)                

#PRINTING ALL THE SETS

# print("original set")
# print(original)
# print("remainder 0 set")
# print(rem0)
# print("remainder 1 set")
# print(rem1)
# print("remainder 2 set")
# print(rem2)
# print("remainder 3 set")
# print(rem3)
# print("remainder 4 set")
# print(rem4)

#CHECKING THE EQUIVALANCE RELATION

original2=set()#another set to compare with original one

for i in rem0:
    original2.add(i)
for i in rem1:
    original2.add(i)
for i in rem2:
    original2.add(i)
for i in rem3:
    original2.add(i)
for i in rem4:
    original2.add(i)                

#COMPARING

if original==original2:
    print("correct code")
else:
    print("error")    