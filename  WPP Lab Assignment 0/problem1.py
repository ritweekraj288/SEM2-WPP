#CODEDOCS ADMIN KIDNAP

T=int(input("enter total number of testcases "))

#CONSTRAINT FOR TESTCASE

while not(T>=1 and T<=100):
    print("wrong entry")
    print("value of test case can be between 1 to 100 only")
    T=int(input("enter total number of testcases "))

#CODING FOR EACH TEST CASE

for i in range (T):
    print("TESTCASE ",i+1)
    N,X,S=int(input("enter total number of boxes that magician is having [between 2 to 105] ")),int(input("enter the box number in which magician placed the golden coin [between 1 to N] ")),int(input("enter the total number swaps performed [between 1 to 104] "))
    
    #CONSTRAINT FOR N , X AND S

    while not((N>=5 and N<=105)and(S>=1 and S<=104)and(X>1 and X<N)):
        print("enter the values on the basis of constraints")
        print("total boxes are",N)
        print("box number in which gold coin was placed is",X)
        print("total swaps performed is",S)


    #TAKING ENTRIES FOR SWAPPING 

    for a in range(S):
        A=int(input("enter the new box number in which gold coin is present [between 1 to N] "))
        B=int(input("enter the box number from which gold coin is replaced [between 1 to N] "))
        gold=A  #GOLD KEEPS A TRACK RECORD OF GOLD COIN

        #CONSTRAINTS FOR A AND B

        while not((A>=1 and A<=N)and(B>=1 and B<=N)):
            print("enter the values following the constraints")
            A=int(input("enter the new box number in which gold coin is present [between 1 to N] "))
            B=int(input("enter the box number from which gold coin is replaced [between 1 to N] "))
            gold=A
        

    #PRINTING THE FINAL RESULT

    print("at last the coin was in box number",gold)      


