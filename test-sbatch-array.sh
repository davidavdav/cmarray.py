#!/bin/sh

mkdir -p out log
sbatch --array=1-24 -o 'out/%a.out' -e 'log/%a.log' ./test.py
