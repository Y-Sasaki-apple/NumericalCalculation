#  -*- coding:utf-8 -*-

from numpy import arange
import csv
Xn = []
Yn = []
with open('inputlag.csv', 'r') as infile:
    reader = csv.reader(infile)
    for row in reader:
        Xn.append(float(row[0]))
        Yn.append(float(row[1]))


def f(x):
    fx = 0
    for xi, yi in zip(Xn, Yn):
        fnx = 1
        for xj in Xn:
            if xi == xj:
                continue
            fnx *= (x-xj)
        fnxn = 1
        for xj in Xn:
            if xi == xj:
                continue
            fnxn *= (xi-xj)
        fx += yi*fnx/fnxn
    return fx

fxlist = [[]]
for x in arange(-1.0, 3.0+1e-5, 0.1):
    fxlist.append([x, f(x)])

with open('outlag.csv', 'w') as outfile:
    writer = csv.writer(outfile, lineterminator='\n')  # 改行コード（\n）を指定しておく
    for fx1 in fxlist:
        writer.writerow(fx1)     # list（1次元配列）の場合
