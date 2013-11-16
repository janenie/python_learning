#!usr/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits

names = ('Jane', 'John', 'Ann');
print names[2]

print names*3

a = 'abcde'
i = -1
for i in [None] + range(-1, -len(a), -1):
  print a[:i]

print 'Welcome to the identifier checker'
print 'Testees must be at least 2 chars long'
my_input = raw_input('identifier to test?')

if (len(my_input) > 1) :
  
  if my_input[0] not in alphas:
    print '''Invalid: first symbol must be alphabetics'''
  else:
  
    for otherChar in my_input[1:]:
      if otherChar not in alphas + nums:
        print '''Invalid: remaining symbols must be alphabetics'''
        break
        
    else:
      print 'Okay as an identifier'
        
print r'\n'

aList = [123, 'abc', 4.56, 7-9j]
print aList
anotherList = [None, 'something to see here']
print anotherList

#add an element
aList[2] = 'float replacer'
print aList

anotherList.append('Hi I am here')
print anotherList

#delete an element
del aList[1]
print aList

aList.remove(123)
print aList

anotherList.pop(0)

anotherList.extend(aList)


