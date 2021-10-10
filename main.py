#! /usr/bin/python3
import re

def makeNice(s):
    return re.subn('(#U[0-9a-f]{4})', lambda cp: chr(int(cp.groups()[0][2:],16)), s) [0]

a = '-#U2605-#U79c1-'
print(a, makeNice(a))
