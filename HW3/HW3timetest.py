## P398 Homework Assignment 3
## Matthias Orlowski
## Execute sorting algorithms defined in HW3sorts.py and take runtimes for lists created using the functions in HW3random.py 

#! /usr/bin/python

import time
import csv
import HW3sorts
import HW3random

lengths1 = range(128,8192,128)
unique_ratio = 0.075
not_sorted_ratio = 0.85

timesBsort1 = []
timesBsort2 = []
timesBsort3 = []
timesBsort4 = []

timesIsort1 = []
timesIsort2 = []
timesIsort3 = []
timesIsort4 = []

timesQsort1 = []
timesQsort2 = []
timesQsort3 = []
timesQsort4 = []

timesQRsort1 = []
timesQRsort2 = []
timesQRsort3 = []
timesQRsort4 = []

temp = []

for i in range(0,len(lengths1)):
    shape1 = [0] * 3
    shape2 = [0] * 3
    shape3 = [0] * 3
    shape4 = [0] * 3
    for k in range(0,3):
        shape1[k] = HW3random.randList(lengths1[i])
        shape2[k] = HW3random.repList(lengths1[i],unique_ratio)
        shape3[k] = HW3random.sortList(lengths1[i],not_sorted_ratio)
        shape4[k] = HW3random.sortListRep(lengths1[i],unique_ratio,not_sorted_ratio)

# bubble sort
    timesBsort1.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.bubbleSort(shape1[k])
        end = time.time()
        temp.append(end - start)
    timesBsort1.append(sum(temp)/3)
    temp = []

    timesBsort2.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.bubbleSort(shape2[k])
        end = time.time()
        temp.append(end - start)
    timesBsort2.append(sum(temp)/3)
    temp = []

    timesBsort3.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.bubbleSort(shape3[k])
        end = time.time()
        temp.append(end - start)
    timesBsort3.append(sum(temp)/3)
    temp = []

    timesBsort4.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.bubbleSort(shape4[k])
        end = time.time()
        temp.append(end - start)
    timesBsort4.append(sum(temp)/3)
    temp = []

    #insertion Sort
    timesIsort1.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.insertionSort(shape1[k])
        end = time.time()
        temp.append(end - start)
    timesIsort1.append(sum(temp)/3)
    temp = []

    timesIsort2.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.insertionSort(shape2[k])
        end = time.time()
        temp.append(end - start)
    timesIsort2.append(sum(temp)/3)
    temp = []

    timesIsort3.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.insertionSort(shape3[k])
        end = time.time()
        temp.append(end - start)
    timesIsort3.append(sum(temp)/3)
    temp = []

    timesIsort4.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.insertionSort(shape4[k])
        end = time.time()
        temp.append(end - start)
    timesIsort4.append(sum(temp)/3)
    temp = []

    #quickSort
    timesQsort1.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.quickSort(shape1[k])
        end = time.time()
        temp.append(end - start)
    timesQsort1.append(sum(temp)/3)
    temp = []

    timesQsort2.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.quickSort(shape2[k])
        end = time.time()
        temp.append(end - start)
    timesQsort2.append(sum(temp)/3)
    temp = []

    timesQsort3.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.quickSort(shape3[k])
        end = time.time()
        temp.append(end - start)
    timesQsort3.append(sum(temp)/3)
    temp = []

    timesQsort4.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.quickSort(shape4[k])
        end = time.time()
        temp.append(end - start)
    timesQsort4.append(sum(temp)/3)
    temp = []

    #quickSortRP
    timesQRsort1.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.quickSortRP(shape1[k])
        end = time.time()
        temp.append(end - start)
    timesQRsort1.append(sum(temp)/3)
    temp = []

    timesQRsort2.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.quickSortRP(shape2[k])
        end = time.time()
        temp.append(end - start)
    timesQRsort2.append(sum(temp)/3)
    temp = []

    timesQRsort3.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.quickSortRP(shape3[k])
        end = time.time()
        temp.append(end - start)
    timesQRsort3.append(sum(temp)/3)
    temp = []

    timesQRsort4.append(lengths1[i])
    for k in range(0,3):
        start = time.time()
        HW3sorts.quickSortRP(shape4[k])
        end = time.time()
        temp.append(end - start)
    timesQRsort4.append(sum(temp)/3)
    temp = []

# create data array
even = range(0,len(timesBsort1),2)
runtimes=[]
for i in even:
    runtimes.append(["Bubble Sort","Random list",timesBsort1[i],timesBsort1[i+1]])
    runtimes.append(["Bubble Sort","Repetitions list",timesBsort2[i],timesBsort2[i+1]])
    runtimes.append(["Bubble Sort","Sorted list",timesBsort3[i],timesBsort3[i+1]])
    runtimes.append(["Bubble Sort","Sorted rep. list",timesBsort4[i],timesBsort4[i+1]])
    # insertion sort
    runtimes.append(["Insertion Sort","Random list",timesIsort1[i],timesIsort1[i+1]])
    runtimes.append(["Insertion Sort","Repetitions list",timesIsort2[i],timesIsort2[i+1]])
    runtimes.append(["Insertion Sort","Sorted list",timesIsort3[i],timesIsort3[i+1]])
    runtimes.append(["Insertion Sort","Sorted rep. list",timesIsort4[i],timesIsort4[i+1]])
    # quick sort
    runtimes.append(["Qick Sort","Random list",timesQsort1[i],timesQsort1[i+1]])
    runtimes.append(["Qick Sort","Repetitions list",timesQsort2[i],timesQsort2[i+1]])
    runtimes.append(["Qick Sort","Sorted list",timesQsort3[i],timesQsort3[i+1]])
    runtimes.append(["Qick Sort","Sorted rep. list",timesQsort4[i],timesQsort4[i+1]])
    # quick sort rp
    runtimes.append(["Qick Sort (RP)","Random list",timesQRsort1[i],timesQRsort1[i+1]])
    runtimes.append(["Qick Sort (RP)","Repetitions list",timesQRsort2[i],timesQRsort2[i+1]])
    runtimes.append(["Qick Sort (RP)","Sorted list",timesQRsort3[i],timesQRsort3[i+1]])
    runtimes.append(["Qick Sort (RP)","Sorted rep. list",timesQRsort4[i],timesQRsort4[i+1]])
    
with open('runtimes.csv','wb') as outp:
    csvWriter = csv.writer(outp)
    for i in runtimes:
        csvWriter.writerow(i)
