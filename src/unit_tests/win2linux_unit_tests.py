import unittest

class TestCdCommand(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'OO')

if __name__ == "__main__":
    unittest.main()