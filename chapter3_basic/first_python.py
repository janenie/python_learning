#/usr/bin/env python

"this is a first python program"

import sys
import os

debug = True

#define a class
class FooClass (object):
  "FooClass"
  version = 0.1
  def __init__(self, nm='John Doe'):
    self.name = nm #class instance
    print 'Create a class instance for ', nm
  def showname(self):
    """display instance attribute and class name"""
    print 'Your name is ', self.name
    print 'My name is ', self.__class__.__name__

#define a function
def addMe2Me(x):
  return x+x

if __name__ == '__main__':
  foo = FooClass()
  foo.showname()
  print addMe2Me(2)
  