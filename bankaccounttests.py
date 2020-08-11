import unittest
import bankaccount


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
        testAccount = bankaccount.BankAccount()
        testAccount.deposit(25)
        testAccount.withdraw(10)
        self.assertEqual(testAccount.balance, 15)


if __name__ == "__main__":
    unittest.main()
