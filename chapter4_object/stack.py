#!/usr/bin/env python

'''act like stack'''
stack = []

def push_it():
  stack.append(raw_input('Enter a new string').strip())

def pop_it():
  print 'pop here'
  if len(stack) == 0:
    print 'No element in stack, cannot pop'
  else:
    print 'Removed['+ stack.pop() +']'

def view_stack():
  print stack

CMDs = {'u': push_it, 'o': pop_it, 'v': view_stack}

def show_menu():
  pr = '''
    P(U)sh
    P(O)p
    (V)iew
    (Q)uit
    Enter choice'''
    
  while True:
    while True:
      try:
        choice = raw_input(pr).strip()[0].lower()
        print choice
      except (EOFError, KeyboardInterrupt, IndexError):
        choice = 'q'
        
      print '\nYou picked: [%s]' % choice
        
      if choice not in 'uovq':
        print 'Invalid input, try again'
      else:
        break
    if (choice == 'q'):
        break
    CMDs[choice]()

if __name__ == '__main__':
  show_menu()
