import datetime


class BankAccount:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        self.transactions = []

    def deposit(self, amount, date=None):
        Transaction.transaction(self, amount, date, "deposit")

    def withdraw(self, amount, date=None):
        Transaction.transaction(self, amount, date, "withdraw")

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


class Transaction:

    def transaction(account, amount, date, type):
        Transaction.__update_balance(account, amount, type)
        Transaction.__add_transaction(
                                    account,
                                    Transaction.__format_date(date),
                                    amount,
                                    type
                                    )

    def __update_balance(account, amount, type):
        if type == "deposit":
            account.balance += amount
        elif type == "withdraw":
            account.balance -= amount

    def __add_transaction(account, date, amount, type):
        transaction_data = {
                            'date': date,
                            'amount': amount,
                            'balance': account.balance,
                            'type': type
                            }
        account.transactions.append(transaction_data)

    def __format_date(date):
        if date is None:
            return datetime.date.today()
        else:
            return datetime.datetime.strptime(date, '%d/%m/%Y')
