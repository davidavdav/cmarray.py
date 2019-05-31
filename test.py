#!/usr/bin/env python
# test.py (c) 2016 David A. van Leeuwen 

## Test script that shows how you can distribute independent python computations in the outer loop
## over a cluster using either SGE or Slurm as cluster manager.

## The idea is that you submit this python script as-is to the batch array submission tool (qsub or sbatch).
## The iterator-wrapper `cmarray` will figure out which items the array-instance is supposed to carry out. 

from __future__ import print_function
from builtins import range
from cmarray import cmarray, start, cmskip
import time

## define the iterator, that iterates over independent computations
r = list(range(821))

## First method: use iterator wrapper
for i in cmarray(r):
    print(start, i)
    time.sleep(0.1)

## Second method: poll if we need to skip this iteration ourselves
for i in r:
    if cmskip(i):
        continue
    print(start, i)
    time.sleep(0.1)

