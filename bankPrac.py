# Assignment -1 - Python. Submission date: 2nd Sep , push code in github and with screen shot  out puts
# 9:49
# Assignment: Bank Account System (OOP in Python)
# Problem Statement
# You are required to build a Python program that simulates a Bank Account system using Object-Oriented Programming (OOP) concepts. The system should support different types of bank accounts and their basic operations.
# Requirements
# Create a base class BankAccount:
# Attributes:
# account_number
# account_holder
# balance (default 0.0)
# Methods:
# deposit(amount) → adds money to the account.
# withdraw(amount) → deducts money if sufficient balance is available.
# get_balance() → returns the current balance.
# __str__() → return account details in string format.
# Create a subclass SavingsAccount (inherits BankAccount):
# Extra Attribute:
# interest_rate
# Extra Method:
# apply_interest() → increases balance based on interest rate.
# Create another subclass CurrentAccount (inherits BankAccount):
# Extra Attribute:
# overdraft_limit
# Modify withdraw(amount) so that account holders can withdraw beyond their balance up to the overdraft limit.
# Create a test program that:
# Creates one savings account and one current account.
# Performs deposit, withdrawal, and balance checks.
# Demonstrates apply_interest() on savings.
# Demonstrates overdraft facility on current account.
# 9:51
# Tasks for You
# Implement the code above.
# Add exception handling (e.g., negative deposits or withdrawals).
# Extend the system by adding another account type (e.g., Fixed Deposit Account with lock-in period).
# Allow multiple accounts in a Bank class and implement transfer_funds() between two accounts.
import random

class BankAccount:
    def __init__(self,account_name):
        self.account_name=account_name.title()
        self.account_number=int(random.randint(10**9, 10**10 - 1))
        self.balance=0.0
    def deposit(self,amt):
        self.balance+=amt
        print(f"Your current balance is {self.balance}")
    def withdraw(self,amt):
        if self.balance-amt<0:
            print("Insuffecient balance")
        else:
            self.balance-=amt
    def account_detail(self):
        print(f"Account holder: {self.account_name} Account Number: {self.account_number} Account Balance: {self.balance}")
class CurrentAccount(BankAccount):
    def __init__(self,account_name):
        self.overdraft=0.0
        super().__init__(account_name)
    def withdraw(self,amt):
        if self.overdraft!=0:
            self.overdraft=self.overdraft-amt
            self.balance=0.0
        elif self.balance-amt<0:
            self.overdraft=self.balance-amt
            self.balance=0.0
        else:
            self.balance-=amt
    def deposit(self,amt):
        if self.overdraft!=0:
            self.overdraft=self.overdraft+amt
            if self.overdraft>0:
                self.balance=self.overdraft+amt
                self.overdraft=0.0
        else:
          self.balance+=amt
        print(f"Your current balance is {self.balance}")
    def overdrf(self):
        print(f"Overdraft Amount {self.overdraft}")
class Bank:
    def __init__(self):
        self.dict={}
        
    def addAcc(self,o1):
        self.dict[o1.account_number]=o1
    
    def transfer(self,account_number1,account_number2,amt):
        if account_number1 in self.dict and account_number2 in self.dict:
            o1=self.dict[account_number1]
            o2=self.dict[account_number2]
            if o1.balance<amt:
                print("Transaction failed due to insufficient balance")
            else:
                o1.balance-=amt
                o2.balance+=amt
                print("Transaction done successfully")

a1=BankAccount("kumaran")
a1.account_detail()
a1.deposit(0)
a1.account_detail()
a1.withdraw(32)
a1.account_detail()
a2=CurrentAccount("kumaran2")
a2.account_detail()
a2.deposit(1000)
a2.account_detail()
a2.withdraw(10)
a2.account_detail()
a2.overdrf()
a3=Bank()
a3.addAcc(a1)
a3.addAcc(a2)
a3.transfer(a1.account_number,a2.account_number,100)
a1.account_detail()
