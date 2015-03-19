import os
import pandas

from filereader import FileReader
from utils import INPUT_DIR, OUTPUT_WORDCOUNTER_PATH

class WordCounter(FileReader):
    '''
    A FileReader that records word frequency from input files
    '''
    def __init__(self, source_dir=INPUT_DIR, out_path=OUTPUT_WORDCOUNTER_PATH):
        self.source_dir = source_dir
        self.out_path = out_path


