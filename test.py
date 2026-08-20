import unittest 
import os
import sys
import validation_functions
from validation_functions import RECOGNIZED_SS_FILES

class TestSupportedExtensions(unittest.TestCase):
    def setUp(self):
        self.mgba = [f".ss{i}" for i in range(1, 10)]
        self.desmume = [f".ds{i}" for i in range(0, 10)]

    def test_num_of_extensions(self):
        self.assertEqual(len(RECOGNIZED_SS_FILES), 9)

    # def test_mgba_extensions(self):


# class TestValidationMethods(unittest.TestCase):
#     def test_help

if __name__ == '__main__':
    unittest.main()