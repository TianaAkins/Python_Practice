from division import division_cal
import unittest

class Test_Division(unittest.TestCase):
    def test_number(self):
        test_case_arg1 = 10
        test_case_arg2 = 2
        expected = 5
        self.assertEqual(division_cal(test_case_arg1, test_case_arg2), expected)

unittest.main() 
