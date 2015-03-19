#!/usr/bin/python
import unittest, sys, os
import filereader
from .utils import INPUT_DIR, OUTPUT_PATH

class TestFileReader(unittest.TestCase):
    def setUp(self):
        self.fr = filereader.FileReader()

    def test_filereader(self):
        #raise AssertionError()
        self.fr._read(INPUT_DIR)
        self.fr.run()
        pass

if __name__ == '__main__':
    unittest.main()
