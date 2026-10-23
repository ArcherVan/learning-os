import unittest
from is_pass import is_pass

class TestIsPass(unittest.TestCase):
    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            is_pass(101)
        with self.assertRaises(ValueError):
            is_pass(-1)
        self.assertTrue(is_pass(60))
        self.assertTrue(is_pass(100))
        self.assertFalse(is_pass(0))
        self.assertFalse(is_pass(59))


        
if __name__ == "__main__":
    unittest.main()