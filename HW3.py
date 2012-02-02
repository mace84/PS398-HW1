## P398 Homework Assignment 3
## Matthias Orlowski
## Implementation and test of two sorting algorithms () 
## Algorithms wer implemented according to: http://www.sorting-algorithms.com/

import random

# O(n^2) algorithm
def insertionSort(list):
    n = len(list)
    for i in range(1,n):
        k = i
        for k in range(k,0,-1):
            if k > 0 and list[k] < list[k-1]:
                list[k], list[k-1] = list[k-1],list[k]
    return list


#O(n^2) to O(n*log2(n)) algorithm
def q3Sort(list):
    n = len(list)
    pivot = random.randrange(1,n)
    list[n],list[pivot] = list[pivot], list[n]

    i = 1; k = i; p = n
    while i < p:
        for i in range(0,1):
            if list[i] < list[n]:
                list[i], list[k] = list[k], list[i]
                k += 1
                break
            elif list[i] == a[n]:
                p -= 1
                list[i], list[p] = list[p], list[i]
                break

    m = min(p-k,n-p+1)
    
                
                
        
