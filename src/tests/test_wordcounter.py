#!/usr/bin/python
import unittest, sys, os
import filereader
from .utils import INPUT_DIR, OUTPUT_DIR

class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.wc = filereader.WordCounter()

    def test_filereader(self):
        self.wc.run()
        pass

if __name__ == '__main__':
    unittest.main()
