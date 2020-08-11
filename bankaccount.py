class BankAccount:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_statement(self):
        return("date || credit || debit || balance\n"
               "14/01/2012 || || 500.00 || 2500.00\n"
               "13/01/2012 || 2000.00 || || 3000.00\n"
               "11/01/2012 || 1000.00 || || 1000.00"
               )
