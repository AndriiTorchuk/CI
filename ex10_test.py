"""
Exercise 10. Test Driven Development
"""

from ex10 import Account
import unittest

class TestAccount(unittest.TestCase):
    def test_account_can_be_created(self):
        account = Account()

if __name__ == '__main__':
    unittest.main()
