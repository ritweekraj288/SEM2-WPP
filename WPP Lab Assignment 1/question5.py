#FUN TASK WITH STUDENTS' NAME IN CLASS

name=[]# list to store names

n=int(input("enter the number of students\t"))

#USING FOR LOOP TO TAKE ENTRY FROM THE USER

for i in range(n):
    stuname=input("enter student's name\t")#student name
    name.append(stuname)

#FUN TASKS

for i in name:
    slice=i[0:16:1]#slicing
    print(slice[::-1])
    
    
    