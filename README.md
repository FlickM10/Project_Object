# BankAccount – Minimal OOP Example

A lightweight Python class demonstrating core object-oriented principles through a realistic banking scenario.

### Features
- Account creation with owner name and optional initial balance
- `deposit(amount)` – adds positive amounts to the balance
- `withdraw(amount)` – deducts amount only if sufficient funds exist
- `transfer(amount, to_account)` – atomic transfer between two BankAccount instances

### Code
```python
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
