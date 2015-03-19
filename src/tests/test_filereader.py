#!/usr/bin/python
import unittest, sys
import filereader

class TestFileReader(unittest.TestCase):
    def setUp(self):
        pass

    def test_filereader(self):
        #raise AssertionError()
        filereader.print_path()
        pass

if __name__ == '__main__':
    unittest.main()