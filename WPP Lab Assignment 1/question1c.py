#STORING PATTERN OF 26 ALPHABETS IN LIST

alpha=[] #empty list

#USING FOR LOOP

track=1 #to keep a track of strings
for i in range(97,123):
    st=str(chr(i)*track) #string to be appended
    alpha.append(st)
    track+=1

#PRINTING FINAL LIST OF STRINGS

print(alpha)