""" Create a class Account.  Two child classes:
SavingsAccount and CurrentAccount.Each implements withdrawal and balance checking."""
class Account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

class Savings(Account):
    def __init__(self,name,balance):
        print(f"----- Welcome {name} ----- \n Type : Savings ")
        super().__init__(name,balance)
    def checkBalance(self):
        print(f"Total Balance : {self.balance} ")
    def withDraw(self):
        amt = int(input("Enter Amount To Withdraw : "))
        print(f"{amt} Withdrawn Successfully ! ")
        self.balance = (self.balance) - amt
        a = input("Want To Check Remaining Balance (Y/N) : ").upper()
        if a=='Y':
            return self.checkBalance()
        else:
            print(f"Thank You {self.name}")
            print("Visit Again !")

class Current(Account):
    def __init__(self,name,balance):
        print(f"----- Welcome {name} ----- \n Type : Current ")
        super().__init__(name,balance)
    def checkBalance(self):
        print(f"Total Balance : {self.balance}")
    def withDraw(self):
        amt = int(input("Enter Amount To Withdraw : "))
        self.balance = (self.balance) - amt
        print(f"{amt} Withdrawn Successfully")
        a = input("Want To Check Remaining Balance (Y/N) : ").upper()
        if a=='Y':
            return self.checkBalance()
        else:
            print(f"Thank You {self.name}")
            print("Visit Again !")


C1 = Savings("Mayank",10500)
C1.checkBalance()
C1.withDraw()
C2 = Current("Aman",8541)
C2.checkBalance()
C2.withDraw()
