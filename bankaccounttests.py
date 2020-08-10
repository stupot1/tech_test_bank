import unittest
import bankaccount as bank


class BankAccountTest(unittest.TestCase):

    def test_01_new_account(self):
        testAccount = bank.BankAccount()
        self.assertEqual(type(testAccount), bank.BankAccount)


if __name__ == "__main__":
    unittest.main()
