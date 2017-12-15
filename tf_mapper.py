#!/usr/bin/env python
import sys
import os
import utils


def tfmapper():
  for line in sys.stdin:
    words = utils.get_normalized_words(line)
    for word in words:
      print "%s\t%s\t1" % (word, utils.filename_from_path(os.getenv('map_input_file','noname')))
if __name__ == '__main__':
  tfmapper()

