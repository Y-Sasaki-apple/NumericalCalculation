#  -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import csv
import numpy as np


Xn = []
Yn = []
with open('inputsq.csv', 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        Xn.append(float(row[0]))
        Yn.append(float(row[1]))
Xl = []
Yl = []
for i in range(5):
    Xl.append([])
    Yl.append([])
    with open('sq_ex2/dim{}_out.csv'.format(i), 'r') as outfile:
        reader = csv.reader(outfile)
        for row in reader:
            if row == []:
                continue
            Xl[i].append(float(row[0]))
            Yl[i].append(float(row[1]))

fp = FontProperties(fname='C:/WINDOWS/Fonts/msgothic.ttc', size=14)

fig, ax = plt.subplots()
plt.scatter(Xn, Yn,marker='o',s=30)
ax.grid()
lines = plt.plot(Xl[0], Yl[0],Xl[1], Yl[1],Xl[2], Yl[2],Xl[3], Yl[3],Xl[4], Yl[4])
#plt.setp(lines[0], linewidth=1, color='r')
plt.legend(('0次近似','1次近似','2次近似','3次近似','4次近似','近似する点'),
           loc='lower right', prop=fp)
ax.set(xlabel='X', ylabel='Y')
plt.savefig("sq.png")
