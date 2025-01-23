#CAPITALIZE EVERY OTHER LETTER OF WORD

#USER INPUT

word=input("enter a word\t")
final=""

#PERFORMING THE OPERATION

index=0#counting
for i in word:
    if index%2==0:
        final+=i
    else:
        final+=i.upper()
    index+=1#updation    

#PRINTING FINAL RESULT

print("final result is",final)