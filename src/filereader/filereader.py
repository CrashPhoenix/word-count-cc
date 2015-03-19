import os
import pandas

def print_path():
    print os.path.join(os.path.dirname(__file__), 'fname')