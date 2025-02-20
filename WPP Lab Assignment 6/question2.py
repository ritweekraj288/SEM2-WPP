import random
class Rock_Paper_Scissors:
    def __init__(self):
        print("starting the game...")
    def game(self,rounds):
        UserPoints=0
        CompPoints=0
        for i in range(1,rounds+1):
            print("playing round",i)
            print("r for rock")
            print("p for paper")
            print("s for scissors")
            user=input("enter your choice:\t")
            comp=random.randint(1,3)
            if comp==1:
                comp="r"
                print("rock from computer")
                if user=="r":
                    print("tie")
                elif user=="p":
                    print("you won")
                    UserPoints+=1
                else:
                    print("you lost")
                    CompPoints+=1
            elif comp==2:     
                comp="p"
                print("paper from computer")
                if user=="p":
                    print("tie")
                elif user=="s":
                    print("you won")
                    UserPoints+=1
                else:
                    print("you lost")
                    CompPoints+=1  
            elif comp==3:
                comp="s"
                print("scissors from computer")
                if user=="s":
                    print("tie")
                elif user=="r":
                    print("you won")
                    UserPoints+=1
                else:
                    print("you lost")
                    CompPoints+=1  
        print("your score is",UserPoints,"and computers score is",CompPoints)
        if UserPoints==CompPoints:
            print("tie")
        elif UserPoints>CompPoints:
            print("you won")
        else:
            print("better luck next time")

S=Rock_Paper_Scissors()
rounds=int(input("enter the number of rounds you want to play:\t"))
S.game(rounds)


                             



