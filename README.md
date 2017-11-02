# sgearray.py
Python wrapper around iterators for simple cluster manager array tasks, analogous to the [Julia version](https://github.com/davidavdav/SGEArrays.jl). 

This should work with both SGE and Slurm.

## Summary

This module makes it easy to submit array jobs for Slurm or Sun Grid Engine in cases you outer script language is Python. 

## Install

```sh
pip install git+https://github.com/davidavdav/cmarray.py.git
```

## Synopsis

Script to be submitted to SGE / Slurm: `script.py`
```python
#!/usr/bin/env python

from sgearray import sgearray

for line in sgearray(open("files.list")):
  file == line.strip()
  ## process `file`
```

Submit this using 

```bash
$ mkdir log
## if you have SGE as cluster manager
$ qsub -e log -o log -t 1-80 python script.py
## if you have Slurm as cluster manager
$ sbatch --array=1-80 -e 'log/%a.log' -o 'out/%a.out' python script.py
```
The first job in the array processes files in `files.list` that are on line 1, 81, etc, the second job processes the file on lines 2, 82 etc.


