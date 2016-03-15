#!/usr/bin/env python
## sgearray (c) 2016 David A. van Leeuwen
## 
## distribute a list over SGE array jobs

import os, logging

issgearray = "SGE_TASK_ID" in os.environ and "SGE_TASK_LAST" in os.environ and os.environ["SGE_TASK_ID"] != "undefined"
if not issgearray:
    start = 0
    step = 1
else:
    start = int(os.environ["SGE_TASK_ID"]) - 1
    step = int(os.environ["SGE_TASK_LAST"])

if start >= step:
    logging.warn("Inconsitent SGE environment variables start %d > step %d", start+1, step)
    
def sgearray(array):
    i = 0
    for element in array:
        if i % step == start:
            yield element
        i += 1

def sgeskip(i):
    return i % step != start

