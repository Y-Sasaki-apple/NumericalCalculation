#  -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
import csv
import numpy as np


Xn = []
Yn = []
with open('outlag.csv', 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        if row == []:
            continue
        Xn.append(float(row[0]))
        Yn.append(float(row[1]))
Xs = []
Ys = []
with open('inputlag.csv', 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        Xs.append(float(row[0]))
        Ys.append(float(row[1]))

Xl = np.linspace(Xn[0], Xn[len(Xn)-1], 500)
Yl = Xl**3-3*Xl**2-Xl+5


fp = FontProperties(fname='C:/WINDOWS/Fonts/msgothic.ttc', size=14)

fig, ax = plt.subplots()
plt.scatter(Xn, Yn,marker='o',s=30)
plt.scatter(Xs, Ys,marker='^',s=150)
lines = plt.plot(Xl, Yl)
plt.setp(lines[0], linewidth=1, color='r')
plt.legend(('補間する関数', 'ラグランジュ補間の出力点','入力の点'),
           loc='upper right', prop=fp)
ax.set(xlabel='X', ylabel='Y')
ax.grid()

plt.savefig("lag.png")
