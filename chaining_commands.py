class user:
    def __init__(self, username):
        self.name = username
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def display_user_balance(self):
        print(self.account_balance)
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def make_transfer(self, amount, transferee):
        self.account_balance -= amount
        transferee.account_balance +=amount
        return self

mason = user("Mason")
sarah = user("Sarah")
kaisa = user("Kaisa")
parker = user("Parker")

mason.make_deposit(100).make_deposit(12).make_deposit(50).make_deposit(100).display_user_balance()

sarah.make_deposit(50).make_deposit(2).make_deposit(25).make_withdrawl(78).display_user_balance()

kaisa.make_deposit(1000).make_withdrawl(500).make_withdrawl(200).make_withdrawl(374).display_user_balance()


mason.make_transfer(amount = 200, transferee= sarah).display_user_balance()
