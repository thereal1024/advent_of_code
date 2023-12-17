#!/usr/bin/env python3

import os
import sys
from shutil import copy2

if __name__ == '__main__':
    date = sys.argv[1]
    directory = '{:02d}'.format(int(date))
    os.mkdir(directory)
    copy2('template/blank.txt', directory + '/input.txt')
    copy2('template/template.py', directory + '/solution.py')
    copy2('template/template.py', directory + '/solution-secondary.py')
