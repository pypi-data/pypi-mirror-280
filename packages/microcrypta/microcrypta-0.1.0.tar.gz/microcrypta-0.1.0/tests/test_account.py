import unittest
from microcrypta.account import Account

class TestAccount(unittest.TestCase):

    def test_account_initialization(self):
        account = Account(1000, 1)
        self.assertEqual(account.size, 1000)
        self.assertEqual(account.risk_percentage, 1)

    def test_get_position_size(self):
        account = Account(1000, 1)
        position_size = account.get_position_size(2)
        self.assertAlmostEqual(position_size, 500.0)

if __name__ == "__main__":
    unittest.main()
