class BankAccount:
    def __init__(self,balance,accno):
        print("starting the managing task...")
        self.balance=balance
        self.accountNumber=accno
    def credit(self,amount):
        self.balance+=amount
        print(amount,"has been credited")
        print("total balance is",self.balance) 
    def debit(self,amount):
        if amount>self.balance:
            print("you have only",self.balance,"rupees in your account which is less than the debited amount")
        else:    
            self.balance-=amount
            print(amount,"has been debited") 
            print("total balance is",self.balance)
    def accountDetail(self):
        print("your account with account number",self.accountNumber,"has a total balance of",self.balance)        

accno=input("enter youe account number:\t")
balance=int(input("enter your balance:\t"))
S=BankAccount(balance,accno)
choice=1
while choice!=0:
    print("1 for credit")
    print("2 for debit")
    print("3 for viewing account details")
    print("0 to exit")
    choice=int(input("enter your choice:\t"))
    if choice==1:
        amount=int(input("enter your amount to be credited:\t"))
        S.credit(amount)
    elif choice==2:
        amount=int(input("enter amount to be debited:\t")) 
        S.debit(amount)   
    elif choice==3:
        S.accountDetail()
print("thankyou...")        