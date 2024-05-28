#!/usr/bin/python
print('Content-type: text/html\n')
from random import random
r = 'your number is: ' + str(random())
print(r)