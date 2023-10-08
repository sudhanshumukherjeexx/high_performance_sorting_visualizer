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

with open('weak_scaling_p1.txt') as f:
    data1 = [list(literal_eval(line)) for line in f]
    val1 = []
    timing1 = []
    for x in data1[0][0]:
        x = int(x)
        val1.append(x)
    for y in data1[0][1]:
        y = float(y)
        timing1.append(y)

with open('weak_scaling_p2.txt') as f:
    data2 = [list(literal_eval(line)) for line in f]
    val2 = []
    timing2 = []
    for x in data2[0][0]:
        x = int(x)
        val2.append(x)
    for y in data2[0][1]:
        y = float(y)
        timing2.append(y)


with open('weak_scaling_p3.txt') as f:
    data3 = [list(literal_eval(line)) for line in f]
    val3 = []
    timing3 = []
    for x in data3[0][0]:
        x = int(x)
        val3.append(x)
    for y in data3[0][1]:
        y = float(y)
        timing3.append(y)


with open('weak_scaling_p4.txt') as f:
    data4 = [list(literal_eval(line)) for line in f]
    val4 = []
    timing4 = []
    for x in data4[0][0]:
        x = int(x)
        val4.append(x)
    for y in data4[0][1]:
        y = float(y)
        timing4.append(y)


with open('weak_scaling_p5.txt') as f:
    data5 = [list(literal_eval(line)) for line in f]
    val5 = []
    timing5 = []
    for x in data5[0][0]:
        x = int(x)
        val5.append(x)
    for y in data1[0][1]:
        y = float(y)
        timing5.append(y)


with open('weak_scaling_p6.txt') as f:
    data6 = [list(literal_eval(line)) for line in f]
    val6 = []
    timing6 = []
    for x in data6[0][0]:
        x = int(x)
        val6.append(x)
    for y in data6[0][1]:
        y = float(y)
        timing6.append(y)




plt.loglog(timing1,p1, marker = '*', label="p=1,N=20K")
plt.loglog(timing2,p2, marker = '*', label="p=2,N=40K")
plt.loglog(timing3,p3, marker = '*' ,label="p=3,N=60K")
plt.loglog(timing4,p4, marker = '*' ,label="p=4,N=80K")
plt.loglog(timing5,p5, marker = '*' ,label="p=5,N=100K")
plt.loglog(timing6,p6, marker = '*' ,label="p=6,N=120K")
plt.xlabel("Timing")
plt.ylabel("Processes")
plt.title("Weak Scaling Test")
plt.legend()
plt.savefig("weak_scaling_test.png")
plt.show()
