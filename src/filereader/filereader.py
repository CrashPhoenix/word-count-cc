import os
import pandas

from utils import INPUT_DIR, OUTPUT_FILEREADER_PATH

class FileReader(object):
    '''
    Abstract class to read files in a directory
    '''
    def __init__(self, source_dir=INPUT_DIR, out_path=OUTPUT_FILEREADER_PATH):
        self.source_dir = source_dir
        self.out_path = out_path

    def run(self, source_dir=None, out_path=None):
        self.source_dir = source_dir if source_dir else self.source_dir
        self.out_path = out_path if out_path else self.out_path
        self._read(self.source_dir)

    def _read(self, path):
        '''
        Read file contents
        '''
        if os.path.isdir(path):
            for dir in sorted(os.listdir(path)):
                self._read(os.path.join(path, dir))
        elif os.path.isfile(path):
            self._process_file(path)

    def _process_file(self, path):
        '''
        Process file
        '''
        with open(self.out_path, 'wb+') as d:
            with open(path) as f:
                for line in f:
                    d.write(line)

    def _normalize(self, word):
        '''
        Cleanse the word
        '''
        return word

