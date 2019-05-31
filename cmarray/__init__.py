#!/usr/bin/env python
## cmarray (c) 2016 David A. van Leeuwen
## 
## distribute a list over SGE or Slurm array jobs

from __future__ import division
from past.utils import old_div
import os, logging

issgearray = "SGE_TASK_ID" in os.environ and "SGE_TASK_LAST" in os.environ and os.environ["SGE_TASK_ID"] != "undefined"

slurmvars = ["SLURM_ARRAY_TASK_ID", "SLURM_ARRAY_TASK_MIN", "SLURM_ARRAY_TASK_MAX", "SLURM_ARRAY_TASK_STEP"]
isslurmarray = set(slurmvars) <= set(os.environ)

if issgearray:
    start = int(os.environ["SGE_TASK_ID"]) - 1
    step = int(os.environ["SGE_TASK_LAST"])
elif isslurmarray:
    id, min, max, slurmstep = [int(os.environ[key]) for key in slurmvars]
    start = id - min
    step = old_div((max - min + 1), slurmstep)
else:
    start = 0
    step = 1

if start >= step:
    logging.warn("Inconsitent cluster manager environment variables start %d > step %d", start+1, step)
    
def cmarray(iterator):
    i = 0
    for element in iterator:
        if i % step == start:
            yield element
        i += 1

def cmskip(i):
    return i % step != start

