#!/usr/bin/env python
class Time60(object):
  def __init__(self, hr, min_):
    self.hr = hr
    self.min = min_
  
  def __str__ (self):
    return '%d:%d' % (self.hr, self.min)
    
  __repr__ = __str__
  
  def __add__ (self, other):
    return self.__class__ (self.hr + other.hr,
      self.min + other.min)
  
  def __iadd__ (self, other):
    self.hr += other.hr
    self.min += other.min
    return self

if __name__ == "__main__":
  mon = Time60(10, 30)
  tue = Time60(11, 50)
  mon += tue
  print mon
  print mon + tue
  