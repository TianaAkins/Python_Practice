from rearrange import rearrange_name
import unittest

class Test_Rearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Akins, Tiana"
        expected = "Tiana Akins"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)
    
    def test_one_name(self):
        testcase = "Tiana"
        expected = "Tiana"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
