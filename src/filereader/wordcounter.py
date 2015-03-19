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
        self.word_counts = {}

    def _process_file(self, path):
        '''
        Process file
        '''
        with open(path) as f:
            for line in f:
                for word in line.strip().split():
                    word = self._normalize(word)
                    self._count_word(word)

        with open(self.out_path, 'wb+') as d:
            for word in sorted(self.word_counts.keys()):
                line = '{0}\t{1}\n'.format(word, self.word_counts[word])
                d.write(line)

    def _count_word(self, word):
        if word in self.word_counts:
            self.word_counts[word] += 1
        else:
            self.word_counts[word] = 1

    def _normalize(self, word):
        '''
        Cleanse the word
        '''
        new_word = ''.join(e for e in word if e.isalpha()).lower()
        return new_word

