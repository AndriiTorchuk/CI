"""
Exercise 10_1.
Test Driven Development
"""

from ex10 import Account
import unittest

class TestAccount(unittest.TestCase):
    #def test_account_can_be_created(self):
    #    account = Account()

    def test_account_object_returns_current_balence(self):
        account = Account("001", 50)
        self.assertEqual(account.account_number, "001")
        self.assertEqual(account.balance, 50)

if __name__ == '__main__':
    unittest.main()
