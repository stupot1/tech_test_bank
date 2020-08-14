import datetime


class Transaction:

    def __init__(self, amount, date, type, balance):
        self.amount = amount
        self.date = Transaction.__format_date(date)
        self.type = type
        self.balance = balance

    def __format_date(date):
        if date is None:
            return datetime.date.today()
        else:
            return datetime.datetime.strptime(date, '%d/%m/%Y')
