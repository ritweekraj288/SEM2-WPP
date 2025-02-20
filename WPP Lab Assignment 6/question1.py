class Password_Manager:
    Password_List=list()
    def __init__(self):
        print("starting the process...")
    def Get_Password(self):
        if self.Password_List==[]:
            print("currently no password has been set...")
        else:    
            return self.Password_List[-1]
    def Set_Password(self,New_Password):
        if New_Password in self.Password_List:
            print("give a new password as this already existed or currently exists...") 
        else:
            self.Password_List.append(New_Password)
            print("new password has been set...")
    def Is_Correct(self,Check_Password):
        if self.Password_List==[]:
            print("no password has been set yet...")
        else:
            if Check_Password==self.Password_List[-1]:
                return True
            else:
                return False

S=Password_Manager()
choice="1"
while choice!="0":
    print("1 for seeing your current password")
    print("2 for setting a new password")
    print("3 for checking your password")
    print("0 for exiting")
    choice=input("enter your choice:\t")
    if choice=="1":
        print(S.Get_Password())
    elif choice=="2":  
        pw=input("enter your new password:\t")
        S.Set_Password(pw)  
    elif choice=="3":
        CheckPW=input("enter your password to be checked:\t")
        print(S.Is_Correct(CheckPW)) 
print("thankyou...")           
