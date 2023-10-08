import numpy as np
import matplotlib.pyplot as plt
from ast import literal_eval

p1 = [1,1,1,1,1]
p2 = [2,2,2,2,2]
p3 = [3,3,3,3,3]
p4 = [4,4,4,4,4]
p5 = [5,5,5,5,5]
p6 = [6,6,6,6,6]
p7 = [7,7,7,7,7]
p8 = [8,8,8,8,8]
with open('strong_scaling_p1.txt') as f:
    data1 = [list(literal_eval(line)) for line in f]
    val1 = []
    timing1 = []
    for x in data1[0][0]:
        x = float(x)
        val1.append(x)
    for y in data1[0][1]:
        y = float(y)
        timing1.append(y)

with open('strong_scaling_p2.txt') as f:
    data2 = [list(literal_eval(line)) for line in f]
    val2 = []
    timing2 = []
    for x in data2[0][0]:
        x = float(x)
        val2.append(x)
    for y in data2[0][1]:
        y = float(y)
        timing2.append(y)


with open('strong_scaling_p3.txt') as f:
    data3 = [list(literal_eval(line)) for line in f]
    val3 = []
    timing3 = []
    for x in data3[0][0]:
        x = float(x)
        val3.append(x)
    for y in data3[0][1]:
        y = float(y)
        timing3.append(y)


with open('strong_scaling_p4.txt') as f:
    data4 = [list(literal_eval(line)) for line in f]
    val4 = []
    timing4 = []
    for x in data4[0][0]:
        x = float(x)
        val4.append(x)
    for y in data4[0][1]:
        y = float(y)
        timing4.append(y)


with open('strong_scaling_p5.txt') as f:
    data5 = [list(literal_eval(line)) for line in f]
    val5 = []
    timing5 = []
    for x in data5[0][0]:
        x = float(x)
        val5.append(x)
    for y in data1[0][1]:
        y = float(y)
        timing5.append(y)


with open('strong_scaling_p6.txt') as f:
    data6 = [list(literal_eval(line)) for line in f]
    val6 = []
    timing6 = []
    for x in data6[0][0]:
        x = float(x)
        val6.append(x)
    for y in data6[0][1]:
        y = float(y)
        timing6.append(y)


with open('strong_scaling_p7.txt') as f:
    data7 = [list(literal_eval(line)) for line in f]
    val7 = []
    timing7 = []
    for x in data7[0][0]:
        x = float(x)
        val7.append(x)
    for y in data7[0][1]:
        y = float(y)
        timing7.append(y)


with open('strong_scaling_p8.txt') as f:
    data8 = [list(literal_eval(line)) for line in f]
    val8 = []
    timing8 = []
    for x in data8[0][0]:
        x = float(x)
        val8.append(x)
    for y in data8[0][1]:
        y = float(y)
        timing8.append(y)


selectionSort_time = []
insertionSort_time = []
heapSort_time = []
countingSort_time = []
cocktailSort_time = []

for i in range(1):
    selectionSort_time.append(timing1[0])
    selectionSort_time.append(timing2[0])
    selectionSort_time.append(timing3[0])
    selectionSort_time.append(timing4[0])
    selectionSort_time.append(timing5[0])
    selectionSort_time.append(timing6[0])
    selectionSort_time.append(timing7[0])
    selectionSort_time.append(timing8[0])

    insertionSort_time.append(timing1[1])
    insertionSort_time.append(timing2[1])
    insertionSort_time.append(timing3[1])
    insertionSort_time.append(timing4[1])
    insertionSort_time.append(timing5[1])
    insertionSort_time.append(timing6[1])
    insertionSort_time.append(timing7[1])
    insertionSort_time.append(timing8[1])

    heapSort_time.append(timing1[2])
    heapSort_time.append(timing2[2])
    heapSort_time.append(timing3[2])
    heapSort_time.append(timing4[2])
    heapSort_time.append(timing5[2])
    heapSort_time.append(timing6[2])
    heapSort_time.append(timing7[2])
    heapSort_time.append(timing8[2])

    countingSort_time.append(timing1[3])
    countingSort_time.append(timing2[3])
    countingSort_time.append(timing3[3])
    countingSort_time.append(timing4[3])
    countingSort_time.append(timing5[3])
    countingSort_time.append(timing6[3])
    countingSort_time.append(timing7[3])
    countingSort_time.append(timing8[3])

    cocktailSort_time.append(timing1[4])
    cocktailSort_time.append(timing2[4])
    cocktailSort_time.append(timing3[4])
    cocktailSort_time.append(timing4[4])
    cocktailSort_time.append(timing5[4])
    cocktailSort_time.append(timing6[4])
    cocktailSort_time.append(timing7[4])
    cocktailSort_time.append(timing8[4])

p=[1,2,3,4,5,6,7,8]
print(selectionSort_time)
plt.loglog(p,selectionSort_time, marker = '*',label="Selection Sort")
plt.loglog(p,insertionSort_time, marker = '*',label="Insertion Sort")
plt.loglog(p,heapSort_time, marker = '*' ,label="Heap Sort")
plt.loglog(p,countingSort_time, marker = '*' ,label="Counting Sort")
plt.loglog(p,cocktailSort_time, marker = '*' ,label="Cocktail Sort")
plt.ylabel("Timing")
plt.xlabel("Processes")
plt.title("Strong Scaling Test for each Algorithm")
plt.legend()
plt.savefig("strong_scaling_test_individual.png")
plt.show()
