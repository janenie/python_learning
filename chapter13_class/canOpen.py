#!/usr/bin/env python

class CanOpen(object):
  def __init__ (self, fn, mode='r', buf=-1):
    self.file = open(fn, mode, buf)
  
  def __str__ (self):
    return str(self.file)
  
  def __repr__ (self):
    return 'self.file'
  #rewrite the function
  def write(self, line):
    self.file.write(line.upper())
  #delegate
  def __getattr__ (self, attr):
    return getattr(self.file, attr)
    
if __name__ == '__main__':
  f = CanOpen('temp.txt', 'w')
  f.write('line has been written')
  f.write('just for testing')
  f.write('which made this short passage')
  f.close()
  
  f = CanOpen('temp.txt', 'r')
  for eachLine in f:
    print eachLine
  