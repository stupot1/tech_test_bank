import datetime


class Statement:

    header = "date || credit || debit || balance"

    def display(self, transactions):
        statement = self.header
        for i in reversed(transactions):
            statement += ("\n")
            statement += (f"{i.date.strftime('%d/%m/%Y')} || ")
            if i.type == "withdraw":
                statement += (f"|| {self.__format_number(i.amount)} || ")
            elif i.type == "deposit":
                statement += (f"{self.__format_number(i.amount)} || || ")
            statement += (f"{self.__format_number(i.balance)}")
        return(statement)

    def __format_number(self, inputNumber):
        return (f"{'%.2f' % inputNumber}")
