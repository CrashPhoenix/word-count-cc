#!/usr/bin/python
import unittest, sys, os
import filereader
from .utils import INPUT_PATH, OUTPUT_PATH

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.fr = filereader.FileReader()

    def test_filereader(self):
        #raise AssertionError()
        assert len(os.listdir(INPUT_PATH)) > 0
        assert len(os.listdir(OUTPUT_PATH)) == 2

if __name__ == '__main__':
    unittest.main()
