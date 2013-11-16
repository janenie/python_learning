#!usr/bin/env python

def safe_float(obj):
  try:
    retval = float(obj)
  except ValueError:
    retval = 'could not convert non-number to float'
  except TypeError:
    retval = 'object type cannot be converted to float'
  return retval
  
if __name__ == '__main__':
  str1 = 'a is a not number'
  print safe_float(str1)
  print safe_float(200L)
  print safe_float({'a': 'Dict'})
  #print safe_float('bad input')



  