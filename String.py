import re

name = input('Input your name\n')

if re.match("^[A-Za-z]*$", name):
    print('Hello,', name)
else:
   print('Incorrect name format entered')