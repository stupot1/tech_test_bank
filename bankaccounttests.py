import unittest
import bankaccount as bank


class BankAccountTest(unittest.TestCase):

    def test_01_new_account(self):
        testAccount = bank.BankAccount()
        self.assertEqual(type(testAccount), bank.BankAccount)

    def test_02_new_account_zero_balance(self):
        testAccount = bank.BankAccount()
        self.assertEqual(testAccount.balance, 0)

    def test_03_new_account_fifty_balance(self):
        testAccount = bank.BankAccount(50)
        self.assertEqual(testAccount.balance, 50)


if __name__ == "__main__":
    unittest.main()
