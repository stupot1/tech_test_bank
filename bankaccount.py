import datetime


class BankAccount:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        transaction_data = {
            'date': datetime.date.today(),
            'amount': amount,
            'balance': self.balance,
            'type': "deposit"
            }
        self.transactions.append(transaction_data)

    def withdraw(self, amount):
        self.balance -= amount
        transaction_data = {
            'date': datetime.date.today(),
            'amount': amount,
            'balance': self.balance,
            'type': "withdraw"
            }
        self.transactions.append(transaction_data)

    def display_statement(self):
        statement = "date || credit || debit || balance"

        for i in reversed(self.transactions):
            statement += ("\n")
            statement += (f"{i['date'].strftime('%d/%m/%Y')} || ")
            if i['type'] == "withdraw":
                statement += (f"|| {'%.2f' % i['amount']} || ")
            elif i['type'] == "deposit":
                statement += (f"{'%.2f' % i['amount']} || || ")
            statement += (f"{'%.2f' % i['balance']}")

        return(statement)
