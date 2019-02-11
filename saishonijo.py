# -*- coding:utf-8-*-

from numpy import arange
import numpy as np
import csv

Xn = []
Yn = []
with open('inputsq.csv', 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        Xn.append(float(row[0]))
        Yn.append(float(row[1]))


Xn = np.asarray(Xn)
Yn = np.asarray(Yn)

dim = 4


def gj(x, j):
    return x**j


G = np.empty((len(Xn), dim))

for xi, i in zip(Xn, range(len(Xn))):
    for j in range(dim):
        G[i, j] = gj(xi, j)


Gt = G.transpose()
invGtG = np.linalg.inv(Gt@G)
a = invGtG@Gt@Yn[:, np.newaxis]


def f(x, a):
    fx = 0
    for i, ai in zip(range(dim), a):
        fx += ai*x**i
    return fx


fxlist = [[]]
for x in arange(-5.0, 5.0+1e-5, 0.1):
    fxlist.append([x, f(x, a)[0]])

with open('outsq.csv', 'w') as outfile:
    writer = csv.writer(outfile, lineterminator='\n')  # 改行コード（\n）を指定しておく
    for fx1 in fxlist:
        writer.writerow(fx1)     # list（1次元配列）の場合
with open('asq.csv', 'w') as afile:
    writer = csv.writer(afile, lineterminator='\n')
    for a1 in a:
        writer.writerow(a1)