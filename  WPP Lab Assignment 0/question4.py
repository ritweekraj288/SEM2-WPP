#SWAPING THE VALUES OF THE TWO VARIABLES

num_1=int(input("enter the first number"))
num_2=int(input("enter the second number"))

#PRINTING THE ENTERED NUMBERS

print("BEFORE SWAPPING")
print("first number is",num_1,"and second number is",num_2)

#SWAPPING PROCESS
  
num_1=num_1+num_2 #WITHOUT USING A SWAP VARIABLE AS A THIRD VARIABLE TO PERFORM THE TASK OF SWAPPING 
num_2=num_1-num_2
num_1=num_1-num_2

#PRINTNG NUMBERS AFTER SWAPPING

print("AFTER SWAPPING")
print("first number is",num_1,"and second number is",num_2)

