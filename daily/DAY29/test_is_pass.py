import unittest
from is_pass import is_pass

class TestIsPass(unittest.TestCase):
    def test_pass1(self):
        self.assertTrue(is_pass(60))

    def test_fail(self):
        self.assertFalse(is_pass(59))

    def test_pass2(self):
        self.assertTrue(is_pass(80))

if __name__ == "__main__":
    unittest.main()