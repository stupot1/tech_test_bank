import unittest
import bankaccount
import datetime


class BankAccountTest(unittest.TestCase):

    def test_01_new_account(self):
        testAccount = bankaccount.BankAccount()
        self.assertEqual(type(testAccount), bankaccount.BankAccount)

    def test_02_new_account_zero_balance(self):
        testAccount = bankaccount.BankAccount()
        self.assertEqual(testAccount.balance, 0)

    def test_03_new_account_fifty_balance(self):
        testAccount = bankaccount.BankAccount(50)
        self.assertEqual(testAccount.balance, 50)

    def test_04_deposit_increments_balance(self):
        testAccount = bankaccount.BankAccount()
        testAccount.deposit(25)
        self.assertEqual(testAccount.balance, 25)

    def test_05_withdraw_decrements_balance(self):
        testAccount = bankaccount.BankAccount(25)
        testAccount.withdraw(10)
        self.assertEqual(testAccount.balance, 15)

    @unittest.expectedFailure
    def test_06_display_statement_dummy_data(self):
        testAccount = bankaccount.BankAccount()
        self.assertEqual(testAccount.display_statement(),
                         "date || credit || debit || balance\n"
                         "14/01/2012 || || 500.00 || 2500.00\n"
                         "13/01/2012 || 2000.00 || || 3000.00\n"
                         "11/01/2012 || 1000.00 || || 1000.00"
                         )

    def test_07_display_statement_real_desposit_amount(self):
        testAccount = bankaccount.BankAccount()
        testAccount.deposit(500)
        self.assertEqual(testAccount.display_statement(),
                         "date || credit || debit || balance\n"
                         "11/08/2020 || 500.00 || || 500.00"
                         )

    def test_08_display_statement_real_withdraw_amount(self):
        testAccount = bankaccount.BankAccount(1000)
        testAccount.withdraw(500)
        self.assertEqual(testAccount.display_statement(),
                         "date || credit || debit || balance\n"
                         "11/08/2020 || || 500.00 || 500.00"
                         )

    def test_09_default_deposit_date_is_today(self):
        testAccount = bankaccount.BankAccount()
        testAccount.deposit(25)
        self.assertEqual(
                         testAccount.transactions[0]['date'],
                         datetime.date.today()
                         )


if __name__ == "__main__":
    unittest.main()
