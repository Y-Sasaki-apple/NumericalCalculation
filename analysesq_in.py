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

fp = FontProperties(fname='C:/WINDOWS/Fonts/msgothic.ttc', size=14)

fig, ax = plt.subplots()
plt.scatter(Xn, Yn,marker='o',s=30)
ax.set(xlabel='X', ylabel='Y')
ax.grid()

plt.savefig("sq_in.png")
