# sgearray.py
Python wrapper around iterators for simple SGE array tasks, analogous to the [Julia version](https://github.com/davidavdav/SGEArrays.jl)

##

This module makes it easy to submit array jobs for Sun Grid Engine in cases you outer script language is Python. 

## Synopsis

Script to be submitted to SGE: `script.py`
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
$ qsub -e log -o log -t 1-80 python script.py
```
The first job in the array processes files in `files.list` that are on line 1, 81, etc, the second job processes the file on lines 2, 82 etc.
