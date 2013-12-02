#!/usr/bin/env python

import thread
from time import ctime, sleep

loops = [4, 2]
#wait for the thread to run over,add lock
def loop(nloop, nsec, lock):
  print 'start loop 0 at time:', ctime()
  sleep(nsec)
  print 'loop ', nloop, ' done at:', ctime()
  lock.release()
    
def main():
  print 'start at', ctime()
  locks = []
  nloops = range(len(loops))
  
  for i in nloops:
    lock = thread.allocate_lock()
    lock.acquire()
    locks.append(lock)
  
  for i in nloops:
    thread.start_new_thread(loop, 
                  (i, loops[i], locks[i]))
  
  for i in nloops:
    while locks[i].locked():
      pass
  
  print 'all DONE at:', ctime()
  
if __name__ == '__main__':
  main()