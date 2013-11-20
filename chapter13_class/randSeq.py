#!/usr/bin/env python

from random import choice

#infinite iteration
class RandSeq(object):
  def __init__ (self, seq):
    self.data = seq
  
  def __iter__ (self):
    return self
  
  def next(self):
    return choice(self.data)
    
class AnyIter(object):
  def __init__(self, data, safe=False):
    self.safe = safe
    self.iter = iter(data)
  
  def __iter__(self):
    return self
  
  def next(self, howmany=1):
    retval = []
    for eachItem in range(howmany):
      try:
        retval.append(self.iter.next())
      except StopIteration:
        if self.safe:
          break
        else:
          raise
    return retval
    
  
if __name__ == "__main__":
  a = AnyIter(range(10))
  i = iter(a)
  for j in range(1, 5):
    print j, ':', i.next(j)
    
  rr = RandSeq(('aaaa', 'bcd', 'google'))
  
  count = 0
  for eachItem in rr:
    print eachItem
    if count == 10:
      break
    count += 1
    
  
  