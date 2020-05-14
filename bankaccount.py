class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("insufficient funds. Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print (f'Your balance is ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.int_rate)
        else:
            print("You are broke. No interest for you!")
        return self

mason = BankAccount(balance=200)
sarah = BankAccount(int_rate = 0.02, balance=350)

mason.deposit(200).deposit(123).deposit(222).yield_interest().display_account_info()
sarah.deposit(100).deposit(100).withdrawl(100).withdrawl(500).yield_interest().display_account_info()



