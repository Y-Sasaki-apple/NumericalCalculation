#  -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import csv
import numpy as np

Xs = []
Ys = []
with open('inputlag.csv', 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        Xs.append(float(row[0]))
        Ys.append(float(row[1]))

Xl = np.linspace(-1, 3, 500)
Yl = Xl**3-3*Xl**2-Xl+5


fp = FontProperties(fname='C:/WINDOWS/Fonts/msgothic.ttc', size=14)

fig, ax = plt.subplots()
plt.scatter(Xs, Ys,marker='^',s=150)
lines = plt.plot(Xl, Yl)
plt.setp(lines[0], linewidth=1, color='r')
plt.legend(('補間する関数','入力の点'),
           loc='upper right', prop=fp)
ax.set(xlabel='X', ylabel='Y')
ax.grid()

plt.savefig("lag_in.png")
