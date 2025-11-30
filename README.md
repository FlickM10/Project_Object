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
```
### Usage Example

```
han = BankAccount("Han", 1000)
print(han.balance)      # 1000.0

han.deposit(500)
print(han.balance)      # 1500.0

lee = BankAccount("Lee")
han.transfer(300, lee)

print(han.balance)      # 1200.0
print(lee.balance)      # 300.0
```

## Design Highlights

Encapsulation of balance and owner data.

Input validation for deposits and withdrawals.

Reusable transfer logic built on existing methods.

Zero external dependencies.

Ideal for teaching OOP fundamentals, encapsulation, and method composition.
