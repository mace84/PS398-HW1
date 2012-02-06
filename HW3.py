## P398 Homework Assignment 3
## Matthias Orlowski
## Implementation and test of two sorting algorithms (Insertion Sort and) 
## Algorithms wer implemented according to: http://www.sorting-algorithms.com/

#! /usr/bin/python

import random
import csv
import timeit

# Exceptions:
class MyException(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)
       
# O(n^2) algorithm
def insertionSort(inlist):
    try:
        if len(inlist) < 2:
            return list
        n = len(inlist)
        for i in range(1,n):
            k = i
            for k in range(k,0,-1):
                if k > 0 and inlist[k] < inlist[k-1]:
                    inlist[k], inlist[k-1] = inlist[k-1],inlist[k]
        return inlist
    except:
        if type(inlist) != list:
            raise MyException, "This function only works in list objects. Please call on a list in the form [1,2,3]."

# timeit.Timer("insertionSort()")


#O(n^2) to O(n) with average O(n*log2(n)) algorithm
def quickSort(inlist):
    try:
        if inlist == []:
            return []
        else:
            pivot = inlist[0]
            lower = quickSort([i for i in inlist[1:] if i < pivot])
            upper = quickSort([i for i in inlist[1:] if i >= pivot])
            return lower + [pivot] + upper
    except:
        if type(inlist) != list:
            raise MyException, "This function only works in list objects. Please call on a list in the form [1,2,3]."


# add random pivot
def quickSortRP(inlist):
    try:
        def qSort(inlist):
            if inlist == []:
                return []
            else:
                pivot = inlist.pop(random.randrange(len(inlist)))
                lower = quickSort([i for i in inlist if i < pivot])
                upper = quickSort([i for i in inlist if i >= pivot])
                return lower + [pivot] + upper
        return qSort(inlist)
    except:
        if type(inlist) != list:
            raise MyException, "This function only works in list objects. Please call on a list in the form [1,2,3]."
