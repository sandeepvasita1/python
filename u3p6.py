class Bank:
    def __init__(self, name, balance):
        self.Name = name
        self.Balance = balance

    def deposit(self, amount):
        self.Balance += amount
        print(f"Deposited: {amount}")
        print(f"New Balance: {self.Balance}")

    def withdraw(self, amount):
        if amount <= self.Balance:
            self.Balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"New Balance: {self.Balance}")
        else:
            print("Insufficient balance")


# Creating an object
account = Bank("sandeep", 5000)

# Deposit
account.deposit(2000)

# Withdrawal
account.withdraw(1500)
