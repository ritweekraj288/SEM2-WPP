#PANGRAMS

sentence=input("enter the sentence\t")#user input
sentence=sentence.lower()#to convert all in lower case
referenceSet=set("abcdefghijklmnopqrstuvwxyz ")#added a space as well

if(set(sentence)==referenceSet):#checking
    print("pangram")
else:
    print("not a pangram")    
