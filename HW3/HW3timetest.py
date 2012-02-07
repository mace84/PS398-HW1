##
##
##

import time
import HW3
import HW3random

lengths1 = range(1000,1201,100)
lengths2 = range(128,65536,128)
unique_ratio = 0.075
not_sorted_ratio = 0.85

outputs1=[[0]*17]*len(lengths1)
for i in range(0,len(lengths1)):
    runtime=[[0]*3]*16
    for j in range(0,2):
        shape1 = HW3random.randList(lengths1[i])
        shape2 = HW3random.repList(lengths1[i],unique_ratio)
        shape3 = HW3random.sortList(lengths1[i],not_sorted_ratio)
        shape4 = HW3random.sortListRep(lengths1[i],unique_ratio,not_sorted_ratio)

# bubble sort
        start = time.time()
        HW3.bubbleSort(shape1)
        end = time.time()
        runtime[0][j] = end - start

        start = time.time()
        HW3.bubbleSort(shape2)
        end = time.time()
        runtime[1][j] = end - start

        start = time.time()
        HW3.bubbleSort(shape3)
        end = time.time()
        runtime[2][j] = end - start

        start = time.time()
        HW3.bubbleSort(shape4)
        end = time.clock()
        runtime[3][j] = end - start

# insertion Sort
        start = time.clock()
        HW3.insertionSort(shape1)
        end = time.clock()
        runtime[4][j] = end - start

        start = time.clock()
        HW3.insertionSort(shape2)
        end = time.clock()
        runtime[5][j] = end - start

        start = time.clock()
        HW3.insertionSort(shape3)
        end = time.clock()
        runtime[6][j] = end - start

        start = time.clock()
        HW3.insertionSort(shape4)
        end = time.clock()
        runtime[7][j] = end - start

# quickSort
        start = time.clock()
        HW3.quickSort(shape1)
        end = time.clock()
        runtime[8][j] = end - start

        start = time.clock()
        HW3.quickSort(shape2)
        end = time.clock()
        runtime[9][j] = end - start

        start = time.clock()
        HW3.quickSort(shape3)
        end = time.clock()
        runtime[10][j] = end - start

        start = time.clock()
        HW3.quickSort(shape4)
        end = time.clock()
        runtime[11][j] = end - start

# quickSortRP
        start = time.clock()
        HW3.quickSortRP(shape1)
        end = time.clock()
        runtime[12][j] = end - start

        start = time.clock()
        HW3.quickSortRP(shape2)
        end = time.clock()
        runtime[13][j] = end - start

        start = time.clock()
        HW3.quickSortRP(shape3)
        end = time.clock()
        runtime[14][j] = end - start

        start = time.clock()
        HW3.quickSortRP(shape4)
        end = time.clock()
        runtime[15][j] = end - start

    outputs1[i][0] = lengths1[i]
    for k in range(0,15):
        outputs1[i][k+1] = sum(runtime[k])/3
