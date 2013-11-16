#!/usr/bin/env python

def safe_float(obj):
  'safe version of float'
  try:
    retval = float(obj)
  except (ValueError, TypeError), diag:
    retval = str(diag)
  return retval

def main():
  'handle all the data processing'
  log = open('cardlog.txt', 'w')
  try:
    try:
      ccfile = open('carddata.txt', 'r')
      txns = ccfile.readlines()
    finally:
      ccfile.close()
  except IOError, e:
    log.write('no txns this month')
    log.close()
  
  # txns = ccfile.readlines()
  # ccfile.close()
  total = 0.0
  log.write('account log:\n')
  
  for eachline in txns:
    result = safe_float(eachline)
    if isinstance(result, float):
      total += result
      log.write('data...processed\n')
    else:
      log.write('ignored: %s' %result)
  print '%.2f (new balance)' %(total)
  log.close
  
if __name__ == '__main__':
  main()