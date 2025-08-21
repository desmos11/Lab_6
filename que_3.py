#Define a class BankAccount with private attributes account_number and
#balance. Implement methods to deposit and withdraw money, ensuring that
#the balance cannot go below zero. Provide a method to get the account
#details. Test the class by performing deposit and withdrawal operations.

class BankAccout:
    def __init__(self,Account_number,balance):
        self.Account_number=Account_number
        self.balance=balance
    def withdraw(self,amount):
        if(amount>0 and self.balance>=amount):
            self.balance-=amount
        else:
            print("Ivalid")
    def deposit(self,amount):
        self.balance+=amount
    def info(self):
        print(f"Account number is {self.Account_number}")
        print(f"Balance is {self.balance}")


account = BankAccout("123456789", 1000)

account.info()
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
account.info()