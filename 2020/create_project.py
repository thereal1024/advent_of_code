#!/usr/bin/env python3

import os
import sys
from shutil import copyfile

if __name__ == '__main__':
    date = sys.argv[1]
    directory = '{:02d}'.format(int(date))
    os.mkdir(directory)
    copyfile('template/input.txt', directory + '/input.txt')
    copyfile('template/template.py', directory + '/solution.py')
    copyfile('template/template.py', directory + '/solution-secondary.py')
