#!/usr/bin/env python

import os

def issgearray():
    return "SGE_TASK_ID" in os.environ and "SGE_TASK_LAST" in os.environ and os.environ["SGE_TASK_ID"] != "undefined"
    
def sgearray(array):
    if not issgearray():
        return array
    start = int(os.environ["SGE_TASK_ID"])-1
    step = int(os.environ["SGE_TASK_LAST"])
    if step < start or step > len(array):
        raise ValueError("Incorrect array parameters")
    return [array[i] for i in range(start, len(array), step)]
