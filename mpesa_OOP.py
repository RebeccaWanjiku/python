from abc import ABC , abstractmethod

# Encapsulation
class Account:
            def __init__(self,account_id,holder_name,balance):
                self.account_id=account_id
                self.holder_name=holder_name
                self.balance=balance
            def deposit(self,amount):
                self.balance +=(amount)
                print(f"Deposited{amount} New Balance{self.balance}")
            def withdraw(self,amount):
                print(f"Withdrawing{amount} New Balance{self.balance}")
                if amount <= self.balance:
                    self.balance-=amount
                else:
                        print("insufficient funds")
            def get_balance(self):
                    return self.balance
            def  get_holder_name(self):
                        return self.holder_name

# inheritance
class Customer (Account):
        def __init__(self,account_id,holder_name,balance,phone_number):
                super().__init__(account_id, holder_name, balance)
                self,phone_number= phone_number

# polymorphism
class Transaction():
     def  __init__(self,amount):
         self.amount=amount
    def execute(self,amount):
                    pass
class Deposittransaction(Transaction):
    def execute(self,account):
            account.deposit()

class WithdrawTranscation(Transaction):
    def execute(self,account):
                    account.withdraw()

#Abatraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_transaction(self,amount):
                pass
class MpesaPaymentsystem(PaymentSystem):
    def process_transaction(self, amount):
            print(f"processing m-pesa payment of {amount}")

# exampleusage
mpesa=MpesaPaymentsystem()
account1=Customer(1,"Martin", 1000,790852445)
deposit=Deposittransaction(500)
withdraw=WithdrawTranscation(100)

deposit.execute(account1)
withdraw.execute(account1)

print(f"balance for {account1.get_holder_name()} is :"
      f"{account1.get_balance()}")
