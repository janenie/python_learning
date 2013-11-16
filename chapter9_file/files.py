#!usr/bin/env python
'''this is for basic file operations '''

FILE = 'file_operation.txt'
CODEC = 'utf-8'

intro = 'This is the basic file operation txt\n'
to_write = open(FILE, 'w')
to_write.write(intro)

main_part = ''' file is read by open()/file() operation
                and open() built-in method recommended
                for more information, please check the 
                website python.org for learning'''
to_write.write(main_part)

to_write.close()

to_read = open(FILE, 'r')
data = [line.strip() for  line in to_read.readlines()]

to_read.close()

for stre in data:
  print stre


