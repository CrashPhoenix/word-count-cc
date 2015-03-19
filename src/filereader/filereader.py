import os
import pandas

from utils import BASE_URL

class FileReader(object):
    '''
    Abstract class to read files
    '''

    def read(self, file_path=''):
        '''
        Read file contents
        '''
        return 'hello'