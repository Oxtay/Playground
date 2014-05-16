#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def Find(pat, str):
  match = re.search(pat, str)
  return match

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  f = open(filename, 'r')
  all_file = f.read()
  match = re.search(r'(<h3.*?>)(.*)</h3>', all_file)
  year_match = re.search(r'Popularity\sin\s(\d\d\d\d)', all_file) # Extracts the year to which the names belong to
  
  if not year_match:
    # We didn't find a year, so we'll exit with an error message.
    sys.stderr.write('Couldn\'t find the year!\n')
    sys.exit(1)
  
  year = year_match.group()
  # Extracting the names and rank numbers
  names = re.findall(r'<tr.*?><td*?>(\d+)</td><td>(\w\w+)</td><td>(\w\w+)', all_file)
  f.close()

  names_dict = {}
  # creating a dict of all the names as keys (be it boy or a girl) and their rank as their value in dict
  for item in names:
    (rank, boyname, girlname) = item
    if boyname not in names_dict:
      names_dict[boyname] = rank
    if girlname not in names_dict:
      names_dict[girlname] = rank

  final_list = [str(year)]

  for key in sorted(names_dict.keys()):
    final_list.append( key + ' ' + names_dict[key] )

  return final_list
  sys.exit(0)
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  for filename in args:
    names = extract_names(filename)
    text = '\n'.join(names)

    if summary: 
      outf = open(filename + '.summary', 'w')
      outf.write(text + '\n')
      outf.close
    else:
      print text

  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
