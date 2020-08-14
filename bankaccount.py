from transaction import Transaction
from statement import Statement


class BankAccount:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        self.transactions = []

    def deposit(self, amount, date=None):
        type = "deposit"
        self.__handle_transaction(amount, date, type)

    def withdraw(self, amount, date=None):
        type = "withdraw"
        self.__handle_transaction(amount, date, type)

    def display_statement(self):
        return Statement.display(Statement(), self.transactions)

    def __handle_transaction(self, amount, date, type):
        self.__update_balance(amount, type)
        t = Transaction(
                        amount,
                        date,
                        type,
                        self.balance
                        )
        self.transactions.append(t)

    def __update_balance(self, amount, type):
        if type == "deposit":
            self.balance += amount
        elif type == "withdraw":
            self.balance -= amount
