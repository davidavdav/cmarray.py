#!/usr/bin/env python
# test.py (c) 2016 David A. van Leeuwen 

from sgearray import sgearray, start, sgeskip
import time

r = range(1000)

for i in sgearray(r):
    print start, i
    time.sleep(1)
    
for i in r:
    if sgeskip(i):
        continue
    print start, i
    time.sleep(1)

