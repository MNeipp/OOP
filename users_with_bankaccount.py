class BankAccount:
    def __init__(self,int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawl(self, amount):
        if self.balance < amount:
            print("insufficient funds. Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print (f'The balance in your account is ${self.balance}')
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.int_rate)
        else:
            print("You are broke. No interest for you!")
        return self

class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.accounts = {}

    def addAccount(self, int_rate = 0.02, balance = 0, type = "checking"):
        # self.int_rate = int_rate
        # self.balance = balance
        self.accounts[type] = BankAccount(int_rate = int_rate, balance = balance)

    def display_account(self):
        for account_type,balance in self.accounts.items():
            print (account_type, end=' '), balance.display_account_info()
            


mason = User("Mason", "ReamusLQ@gmail.com")

mason.addAccount()
mason.addAccount(type = "savings", balance = 300)
mason.addAccount(type="credit", balance = 75)
mason.accounts['checking'].deposit(500)
mason.accounts['savings'].deposit(500)

mason.accounts['checking'].display_account_info()