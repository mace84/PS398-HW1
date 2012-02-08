## P398 Homework Assignment 3
## Matthias Orlowski
## Generate different list structures for runtime tests for different sorting algorithms implemented in HW3sorts.py

#! /usr/bin/python

import random
import numpy

def randList(length):
    pop = numpy.arange(-50000,50000)
    outlist = sample_wr(pop,length)
    return outlist

def repList(length,orgratio):
    origin = int(round(length*orgratio))
    pop = randList(origin)
    outlist = sample_wr(pop,length)
    return outlist

def sortList(length,not_sorted):
    outlist = randList(length)
    outlist = sorted(outlist)
    randrate = int(round(length*not_sorted))
    choice1 = random.sample(range(len(outlist)),randrate)
    choice2 = random.sample(range(len(outlist)),randrate)
    for i in range(len(choice1)):
            outlist[choice1[i]],outlist[choice2[i]] = outlist[choice2[i]], outlist[choice1[i]]
    return outlist

def sortListRep(length,origin,not_sorted):
    outlist = repList(length,origin)
    outlist = sorted(outlist)
    randrate = int(round(length*not_sorted))
    choice1 = random.sample(range(len(outlist)),randrate)
    choice2 = random.sample(range(len(outlist)),randrate)
    for i in range(len(choice1)):
            outlist[choice1[i]],outlist[choice2[i]] = outlist[choice2[i]], outlist[choice1[i]]
    return outlist

def sample_wr(population, size):
    sample = []
    ssize = 0
    while ssize < size:
        sample.append(random.sample(population,1)[0])
        ssize += 1
    return sample
