#!/usr/bin/env python

db = {}

def newuser():
  prompt = 'login desired: '
  while True:
    name = raw_input(prompt)
    if db.has_key(name):
      prompt = 'name taken, try another: '
      continue
    else:
      break;
  pwd = raw_input('password: ')
  db[name] = pwd
  
def olduser():
  name = raw_input('login: ')
  pwd = raw_input('password: ')
  password = db[name]
  if (pwd == password):
    print 'Welcome back ', name
  else:
    print 'login incorrect'

def showmenu():
  prompt = """
  (N) ew User login
  (E) xiting User login
  (Q) uit
  Enter choice """
  done  = False
  while not done:
    chosen = False
    while not chosen:
      try:
        choice = raw_input(prompt).strip()[0].lower()
      except (EOFError, KeyboardInterrupt):
        choice = 'q'
      print '\nYou picked: [%s]' % choice
      if choice not in 'neq':
        print 'Invalid input option, try again'
      else:
        break
    
    if choice == 'q': done = True
    if choice == 'n': newuser()
    if choice == 'e': olduser()
    
if __name__ == '__main__':
  showmenu()