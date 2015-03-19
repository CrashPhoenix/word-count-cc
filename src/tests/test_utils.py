#!/usr/bin/python
import unittest, os
from .utils import INPUT_DIR, OUTPUT_PATH, OUTPUT_DIR

class TestUtils(unittest.TestCase):
    def test_utils(self):
        #raise AssertionError()
        assert len(os.listdir(INPUT_DIR)) > 0
        assert len(os.listdir(OUTPUT_DIR)) >= 2

if __name__ == '__main__':
    unittest.main()