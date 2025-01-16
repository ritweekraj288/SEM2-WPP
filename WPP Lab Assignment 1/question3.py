# CONVERSION OF FEET IN OTHER UNITS USING LIST

feet=float(input("enter lenght in feet\t"))

#OPTIONS

print("choose your option")
print("1 for inches")
print("2 for yards")
print("3 for miles")
print("4 for milimeters")
print("5 for centimeters")
print("6 for meters")
print("7 for kilometers")

#OPTION INPUT FROM USER

option=int(input("enter your option\t"))

#LIST OF FORMULAS

lst=["hello world",feet*12,feet*0.333,feet*0.000189,feet*304.8,feet*30.48,feet*0.305,feet*0.000305]

#PRINTING FINAL RESULT

print("answer is",lst[option])


