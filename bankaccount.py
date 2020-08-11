class BankAccount:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        transaction_data = {
            'amount': amount,
            'balance': self.balance,
            'type': "deposit"
            }
        self.transactions.append(transaction_data)

    def withdraw(self, amount):
        self.balance -= amount
        transaction_data = {
            'amount': amount,
            'balance': self.balance,
            'type': "withdraw"
            }
        self.transactions.append(transaction_data)

    def display_statement(self):
        statement = "date || credit || debit || balance"

        for i in self.transactions:
            statement += ("\n11/08/2020 || ")
            if i['type'] == "withdraw":
                statement += (f"|| {'%.2f' % i['amount']} || ")
            elif i['type'] == "deposit":
                statement += (f"{'%.2f' % i['amount']} || || ")
            statement += (f"{'%.2f' % i['balance']}")

        return(statement)
