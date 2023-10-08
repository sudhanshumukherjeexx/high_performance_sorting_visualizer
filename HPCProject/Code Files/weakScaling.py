import multiprocessing as mp
import matplotlib.pyplot as plt
import random
import time
import numpy as np

numlist = random.sample(range(1,1000000),20000)

#SELECTION SORT ALGORITHM
def selectionSort(array):
    for i in range(len(array)):
        smallestIndex = i
        for j in range(i+1, len(array)):
            if array[j] < array[smallestIndex]:
                smallestIndex = j
        #swapping the elements
        (array[i],array[smallestIndex]) = (array[smallestIndex],array[i])
    return array 

#INSERTION SORT ALGORITHM
def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array

#HEAP SORT ALGORITHM
def heapify(array, n, i):
    # Find largest among root and children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
      largest = left
  
    if right < n and array[largest] < array[right]:
      largest = right
  
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
      array[i], array[largest] = array[largest], array[i]
      heapify(array, n, largest)
    return array

def heapSort(array):
    n = len(array)  
    # Build max heap
    for i in range(n//2, -1, -1):
      heapify(array, n, i)
    for i in range(n-1, 0, -1):
      # Swap
      array[i], array[0] = array[0], array[i]
      # Heapify root element
      heapify(array, i, 0)
    return array

#COUNTING SORT ALGORITHM
def countingSort(array):
    size = len(array)
    output = [0] * size
    # Initialize count array
    count = [0] * 1000000
    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1
    # Store the cummulative count
    for i in range(1, 1000000):
        count[i] += count[i - 1]
    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]        
    return array

#COCKTAIL SORT
def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):

    # reset the swapped flag on entering the loop,
    # because it might be true from a previous
    # iteration.
        swapped = False

        # loop from left to right same as the bubble
        # sort
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # if nothing moved, then array is sorted.
        if (swapped == False):
            break

        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1

        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start + 1
    return a


val = []
timing = []

if __name__ == '__main__':
    pool = mp.Pool()
    pool = mp.Pool(processes=6)
    val = [numlist]
    for i in range(1):
        print("SELECTION SORT ITERATION : ",i+1)
        start = time.time()
        input = [val[i]]
        val.append(len(val[i]))
        output = pool.map(selectionSort,input)
        print("Input : {}\n".format(input))
        print("Output : {}\n".format(output))
        end = time.time() - start
        timing.append(end)
    for i in range(1):
        print("INSERTION SORT ITERATION : ",i+1)
        start = time.time()
        input = [val[i]]
        val.append(len(val[i]))
        output = pool.map(insertionSort,input)
        print("Input : {}\n".format(input))
        print("Output : {}\n".format(output))
        end = time.time() - start
        timing.append(end)
    for i in range(1):
        print("HEAP SORT ITERATION : ",i+1)
        start = time.time()
        input = [val[i]]
        val.append(len(val[i]))
        output = pool.map(heapSort,input)
        print("Input : {}\n".format(input))
        print("Output : {}\n".format(output))
        end = time.time() - start
        timing.append(end)
    for i in range(1):
        print("COUNTING SORT ITERATION : ",i+1)
        start = time.time()
        input = [val[i]]
        val.append(len(val[i]))
        output = pool.map(countingSort,input)
        print("Input : {}\n".format(input))
        print("Output : {}\n".format(output))
        end = time.time() - start
        timing.append(end)
    for i in range(1):
        print("COCKTAIL SORT ITERATION : ",i+1)
        start = time.time()
        input = [val[i]]
        val.append(len(val[i]))
        output = pool.map(cocktailSort,input)
        print("Input : {}\n".format(input))
        print("Output : {}\n".format(output))
        end = time.time() - start
        timing.append(end)
    data = [val, timing] 
    with open('weak_scaling_p1.txt', 'w') as f:
        f.write(str(data))