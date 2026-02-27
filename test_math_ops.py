import unittest
from math_ops import add_num, sub_num

class TestMathOps(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add_num(2, 3), 5)
        self.assertEqual(add_num(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(sub_num(10, 5), 5)
        self.assertEqual(sub_num(15, 7), 8)
        self.assertEqual(sub_num(15, 12), 3)

if __name__ == '__main__':
    unittest.main()
