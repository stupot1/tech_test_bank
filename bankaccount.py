import datetime


class BankAccount:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        self.transactions = []

    def deposit(self, amount, date=None):
        self.balance += amount
        self.__add_transaction(self.__format_date(date), amount, "deposit")

    def withdraw(self, amount, date=None):
        self.balance -= amount
        self.__add_transaction(self.__format_date(date), amount, "withdraw")

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

    def __add_transaction(self, date, amount, type):
        transaction_data = {
                            'date': date,
                            'amount': amount,
                            'balance': self.balance,
                            'type': type
                            }
        self.transactions.append(transaction_data)

    def __format_date(self, date):
        if date is None:
            return datetime.date.today()
        else:
            return datetime.datetime.strptime(date, '%d/%m/%Y')
