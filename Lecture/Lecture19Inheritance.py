"""Inheritance"""
"""Inheritance is best for representing is-a relationship:
    E.g., a chenking account 'is a' specipic type of account.
    So, CheckingAccount inherits from Account
"""
class Account:
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Add amount to balance"""
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Substract amount from balance"""
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            return self.balance

class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

"""Composition"""
"""Composition is best for representing has-a relationship
    E.g., a bank 'has a' collection of bank accounts it manages
    So, a bank has a list of accounts as an attribute.
"""
class Bank:
    """A bank *has* accounts.
    
    >>>bank = Bank()
    >>>john = bank.open_account('John', 10)
    >>>jack = bank.open_account('Jack', 5, CheckingAccount)
    >>>john.interest
    0.02
    >>>jack.interest
    0.01
    >>>bank.pay_interest()
    >>>john.balance
    10.2
    """
    def __init__(self):
        self.accounts = []
    
    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for i in self.accounts:
            i.deposit(i.interest * i.balance)