#!/usr/bin/python

import commands
import sys
import os

def List(dir):
	filenames = os.listdir(dir)
	cmd = 'ls -l ' + dir
	(status, output) = commands.getstatusoutput(cmd)
	print output

def main():
	List(sys.argv[1])

if __name__ == '__main__':
  main()