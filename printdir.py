#!/usr/bin/python
## Example pulls filenames from a dir, prints their relative and absolute paths

import sys
import os

def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print filename  ## foo.txt
    print os.path.join(dir, filename) ## dir/foo.txt (relative to current dir)
    print os.path.abspath(os.path.join(dir, filename)) ## /home/nick/dir/foo.txt

def main():
	printdir(sys.argv[1])

if __name__ == '__main__':
  main()