from abc import ABC, abstractmethod

# Encapsulation
class Account:
    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        print(f"Withdrawing {amount}. Current Balance: {self.balance}")
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def get_holder_name(self):
        return self.holder_name


# Inheritance
class Customer(Account):
    def __init__(self, account_id, holder_name, balance, phone_number):
        super().__init__(account_id, holder_name, balance)
        self.phone_number = phone_number  # Corrected the typo here

# Polymorphism
class Transaction:
    def __init__(self, amount):
        self.amount = amount

    def execute(self, account):
        pass

class DepositTransaction(Transaction):  # Corrected typo here
    def execute(self, account):
        account.deposit(self.amount)  # Pass the amount to the deposit method

class WithdrawTransaction(Transaction):  # Corrected typo here
    def execute(self, account):
        account.withdraw(self.amount)  # Pass the amount to the withdraw method

# Abstraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_transaction(self, amount):
        pass

class MpesaPaymentSystem(PaymentSystem):  # Corrected typo here
    def process_transaction(self, amount):
        print(f"Processing M-Pesa payment of {amount}")

# Example usage
mpesa = MpesaPaymentSystem()  # Corrected class name
account1 = Customer(1, "Martin", 1000, 790852445)
deposit = DepositTransaction(500)
withdraw = WithdrawTransaction(100)

# Execute transactions
deposit.execute(account1)
withdraw.execute(account1)

print(f"Balance for {account1.get_holder_name()} is: {account1.get_balance()}")
