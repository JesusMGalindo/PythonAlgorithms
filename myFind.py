'''
function will return the full paths of all the files containing the specified substring at the command line. It will recursively search all the files and subdirectories starting from the specified directory. At the end of the command, it also returns the total file size of those files found in bytes.  The total file size should be the summation of the file sizes of the regular files only.  That means that you should not include directories for the computation of the total file size.
User can run python3 myFind.py <PATH> <STRING> in terminal.
'''

import os
from os.path import getsize
import sys
import stat
from stat import *

def myFind(startDir, strcmd):
    # get directory
    dir = os.listdir(startDir)
    size = 0
    # loop through directory looking at each path name
    for file in dir:
        path = os.path.join(startDir, file)
        mode = os.stat(path).st_mode
        # if its a directory
        if S_ISDIR(mode):
            # if directory check directoy using recursion
            size += myFind(path, strcmd)
        # if its not a directory
        if S_ISREG(mode):
            # check if string is a substring in file
            if strcmd not in file:
                continue
            # get file and size
            print(path, " -> " , getsize(path), "Bytes")
            
            size += getsize(path)
    return size 
# check is user input appropriate amount of arguments
if len(sys.argv) != 3:
    print("Incorrect amount of arguments.", "\n./myFind.py <PATH> <STRING>")
    exit() 
arg1 = sys.argv[1]
arg2 = sys.argv[2]
totalFileSize = myFind(arg1, arg2)
print("\nTotal files size:", totalFileSize, "Bytes")
