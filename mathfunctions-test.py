import unittest
import mathfunctions


class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mathfunctions.add(5,4), 9, msg="FAILURE")

    def test_multiply(self):
        self.assertEqual(mathfunctions.multiply(3,4), 13, msg="FAILURE")
    
    def test_power(self):
        self.assertEqual(mathfunctions.power(2,8), 12, msg="FAILURE")

if __name__ == '__main__':
    unittest.main()