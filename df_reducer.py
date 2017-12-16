#!/usr/bin/env python
import sys


file_only = sys.argv[1]

def prt_item(item, curcount):
  items = item.split()
  file_name = items[1]
  if file_only != file_name:
    return False
  print "%s\t%d\t%s" % (items[2], curcount, items[0])
  return True

def dfreducer():
  curword = None
  curcount = None
  space = []
  for line in sys.stdin:
    word,filename,wordcount,count = line.strip().split()
    #if (file_only != filename):
    #  continue
    prefix = "%s\t%s\t%s" %(word,filename,wordcount)
    if word == None:
      curword = word
      curcount = eval(count)
      space.append(prefix)
    elif curword == word:
      curcount += eval(count)
      space.append(prefix)
    else:
      for item in space:
        prt_item(item, curcount)
      curword = word
      curcount = eval(count)
      space = [prefix]
  for item in space:
    prt_item(item, curcount)

if __name__=='__main__':
  dfreducer()

