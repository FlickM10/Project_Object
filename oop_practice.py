class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds or invalid amount")

    def transfer(self, amount, to_account):
        self.withdraw(amount)
        to_account.deposit(amount)


han = BankAccount("Han", 1000)  
print(han.balance)              
han.deposit(500)
print(han.balance)               