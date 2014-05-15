#!/usr/bin/python

import sys
import os

def List(dir):
	filenames = os.listdir(dir)
	print filenames

def main():
	List(sys.argv[1])

if __name__ == '__main__':
  main()