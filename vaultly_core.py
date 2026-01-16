# VAULTLY BANKING SYSTEM - CORE LOGIC
# Location: Upington, South Africa

class VaultlyAccount:
    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.pin = pin
        self.balance = balance
        self.history = []

    def get_balance(self):
        return f"R {self.balance:,.2f}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposit: +R{amount:,.2f}")
            return True
        return False

    def transfer(self, amount, recipient):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Transfer to {recipient}: -R{amount:,.2f}")
            return True
        return False

# Quick Test for the Coach
my_vault = VaultlyAccount("User", "1234", 10500)
print(f"Vaultly Active: {my_vault.owner}'s Balance is {my_vault.get_balance()}")
