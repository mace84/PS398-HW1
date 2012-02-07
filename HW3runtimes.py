## P398 Homework Assignment 3
## Matthias Orlowski
## Runtime test for different sorting algorithms implemented in HW3.py

#! /usr/bin/python

import HW3
import random
import timeit
import csv
import itertools
import numpy

def randList(length):
    start = random.uniform(-1000,0)
    end = random.uniform(0,1000)
    steps = start-end/length
    pop = numpy.arange(start,end,steps)
    outlist = sample_wr(pop,1/length)
    return outlist

def repList(length,origin):
    pop = randList(origin)
    outlist = sample_wr(pop,length)
    return outlist

def sortList(length,not_sorted):
    outlist = randList(length)
    print outlist
    outlist = sorted(outlist)
    print outlist
    randrate = length/not_sorted
    choice1 = random.sample(range(len(outlist)),randrate)
    choice2 = random.sample(range(len(outlist)),randrate)
    for i in range(len(choice1)):
            outlist[choice1[i]],outlist[choice2[i]] = outlist[choice2[i]], outlist[choice1[i]]
    return outlist

def sample_wr(population, k):
    n = len(population)
    _random, _int = random.random, int
    return [_int(_random() * n) for i in itertools.repeat(None, k)]

def testInsertionSort()
    testlist = randList(10)
    timeit.Timer(HW3.insertionSort(testlist))

# HW3.bubbleSort()
# HW3.quickSort()
# HW3.quickSortRP()
