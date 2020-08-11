class BankAccount:

    def __init__(self, starting_balance=0):
        self.balance = starting_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        transaction_data = {'credit': amount, 'balance': self.balance}
        self.transactions.append(transaction_data)

    def withdraw(self, amount):
        self.balance -= amount

    def display_statement(self):
        statement = "date || credit || debit || balance\n"

        for i in self.transactions:
            statement += (f"11/08/2020 || {'%.2f' % i['credit']} || || {'%.2f' % i['balance']}")

        return(statement)
