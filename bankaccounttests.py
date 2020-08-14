import unittest
import bankaccount
import datetime


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.testAcc = bankaccount.BankAccount()

    def test_01_new_account(self):
        self.assertEqual(type(self.testAcc), bankaccount.BankAccount)

    def test_02_new_account_zero_balance(self):
        self.assertEqual(self.testAcc.balance, 0)

    def test_03_new_account_fifty_balance(self):
        testAccount = bankaccount.BankAccount(50)
        self.assertEqual(testAccount.balance, 50)

    def test_04_deposit_increments_balance(self):
        self.testAcc.deposit(25)
        self.assertEqual(self.testAcc.balance, 25)

    def test_05_withdraw_decrements_balance(self):
        testAccount = bankaccount.BankAccount(25)
        testAccount.withdraw(10)
        self.assertEqual(testAccount.balance, 15)

    @unittest.expectedFailure
    def test_06_display_statement_dummy_data(self):
        self.assertEqual(self.testAcc.display_statement(),
                         "date || credit || debit || balance\n"
                         "14/01/2012 || || 500.00 || 2500.00\n"
                         "13/01/2012 || 2000.00 || || 3000.00\n"
                         "10/01/2012 || 1000.00 || || 1000.00"
                         )

    def test_07_display_statement_real_desposit_amount(self):
        self.testAcc.deposit(500)
        date = datetime.datetime.today()
        self.assertEqual(self.testAcc.display_statement(),
                         "date || credit || debit || balance\n"
                         f"{date.strftime('%d/%m/%Y')} || 500.00 || || 500.00"
                         )

    def test_08_display_statement_real_withdraw_amount(self):
        testAccount = bankaccount.BankAccount(1000)
        testAccount.withdraw(500)
        date = datetime.datetime.today()
        self.assertEqual(testAccount.display_statement(),
                         "date || credit || debit || balance\n"
                         f"{date.strftime('%d/%m/%Y')} || || 500.00 || 500.00"
                         )

    def test_09_default_deposit_date_is_today(self):
        self.testAcc.deposit(25)
        self.assertEqual(
                         self.testAcc.transactions[0].date,
                         datetime.date.today()
                         )

    def test_10_default_withdraw_date_is_today(self):
        testAccount = bankaccount.BankAccount(50)
        testAccount.withdraw(25)
        self.assertEqual(
                         testAccount.transactions[0].date,
                         datetime.date.today()
                         )

    def test_11_display_statement_real_todays_date_and_amounts(self):
        self.testAcc.deposit(10)
        self.testAcc.withdraw(4)
        date = datetime.datetime.today()
        self.assertEqual(self.testAcc.display_statement(),
                         "date || credit || debit || balance\n"
                         f"{date.strftime('%d/%m/%Y')} || || 4.00 || 6.00\n"
                         f"{date.strftime('%d/%m/%Y')} || 10.00 || || 10.00"
                         )

    def test_12_deposit_date_can_be_specified(self):
        self.testAcc.deposit(25, "10/08/2020")
        self.assertEqual(
                         self.testAcc.transactions[0].date,
                         datetime.datetime(2020, 8, 10, 0, 0)
                         )

    def test_13_withdraw_date_can_be_specified(self):
        testAccount = bankaccount.BankAccount(50)
        testAccount.withdraw(25, "10/08/2020")
        self.assertEqual(
                         testAccount.transactions[0].date,
                         datetime.datetime(2020, 8, 10, 0, 0)
                         )

    def test_14_display_statement_full_real_data(self):
        self.testAcc.deposit(1000, "10/01/2012")
        self.testAcc.deposit(2000, "13/01/2012")
        self.testAcc.withdraw(500, "14/01/2012")
        self.assertEqual(self.testAcc.display_statement(),
                         "date || credit || debit || balance\n"
                         "14/01/2012 || || 500.00 || 2500.00\n"
                         "13/01/2012 || 2000.00 || || 3000.00\n"
                         "10/01/2012 || 1000.00 || || 1000.00"
                         )


if __name__ == "__main__":
    unittest.main()
