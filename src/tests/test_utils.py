#!/usr/bin/python
import unittest, os
from .utils import INPUT_PATH, OUTPUT_PATH

class TestUtils(unittest.TestCase):
    def test_utils(self):
        #raise AssertionError()
        assert len(os.listdir(INPUT_PATH)) > 0
        assert len(os.listdir(OUTPUT_PATH)) == 2

if __name__ == '__main__':
    unittest.main()