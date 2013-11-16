#!/usr/bin/env python

#type checking 
def displayNumType(num):
  print num, 'is',
  if isinstance(num, (int, long, float, complex)):
    print 'a number of type: ', type(num).__name__
  else:
    print 'not a number at all!'

displayNumType(-69)
displayNumType(-52.1+1.0j)
displayNumType('xxxx')

