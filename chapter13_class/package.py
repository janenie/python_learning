#!/usr/bin/env python
from time import time, ctime

class WrapMe (object):
  def __init__ (self, obj):
    self.__data = obj
  
  def get(self):
    return self.__data
  
  def __repr__ (self):
    return 'self.__data'
  
  def __str__ (self):
    return str(self.__data)
  #grant the attribute to object using gettattr() method
  def __getattr__ (self, attr):
    return getattr(self.__data, attr)


class TimeWrapMe(object):
  
  def __init__ (self, obj):
    self.__data = obj
    self.__ctime = self.__mtime = \
      self.__atime = time()
  
  def get(self):
    self.__atime = time()
    return self.__data
  
  def gettimeval(self, t_type):
    if not isinstance(t_type, str) or \
            t_type[0] not in 'cma':
            raise TypeError, \
            "arguments of 'c', 'm', 'a' req'd"
    return getattr(self, '_%s__%stime' % \
            (self.__class__.__name__, t_type[0]))
  
  def gettimestr(self, t_type):
    return ctime(self.gettimeval(t_type))
  
  def set(self, obj):
    self.__data = obj
    self.__mtime = self.__atime = time()
  
  def __repr__ (self):
    self.__atime = time()
    return 'self.__data'
  
  def __str__ (self):
    self.__atime = time()
    return str(self.__data)
  #delegate
  def __getattr__ (self, attr):
    self.__atime = time()
    return getattr(self.__data, attr)



if __name__ == '__main__':
  wrappList = WrapMe(['123', 'foo', 45.67])
  wrappList.append('bar')
  wrappList.append('123')
  
  print wrappList.count('123')
  wrappList.pop()
  print wrappList
  
  realList = wrappList.get()
  print realList[3]
  
  timeWrapObj = TimeWrapMe(932)
  timeWrapObj.gettimestr('c')
  timeWrapObj.gettimestr('m')
  timeWrapObj.gettimestr('a')
  timeWrapObj.set('Time is up')
  print timeWrapObj
  
  
  
  