import sys
import os
import numpy as np

datas = []

def openf(name_file: str):
    with open(name_file) as f:
        data = []
        for line in f:
            data.append([float(x) for x in line.split()])
        for i in range(len(data)):
            for j in range(len(data[i])):
                datas.append(data[i][j])

def percentile(lst):
    perc = np.percentile(lst, 90)
    perc = f'{perc:.{2}f}'
    print(perc)

def median (lst):
    n=len(lst)
    s=sorted(lst)
    k=n//2
    if n%2==0:
        med = (0.5*(s[k]+s[k-1]))
        med = f'{med:.{2}f}'
        print(med)
    else:
        mad = s[k]
        med = f'{med:.{2}f}'
        print(med)

def maximum (lst):
    s = sorted(lst)
    max = len(s)
    max = f'{max:.{2}f}'
    print(max)

def minimum (lst):
    s = sorted(lst)
    min = s[0]
    min = f'{min:.{2}f}'
    print(min)

def mean (lst):
    sum = 0
    i = 0
    for i in range(len(lst)):
        sum += i
    rezult = sum / len(lst)
    rezult = f'{rezult:.{2}f}'
    print(rezult)

if __name__ == "__main__":
    if len (sys.argv) > 1:
        way_to_file = os.path.dirname(sys.argv[1])
        name_f = os.path.basename(sys.argv[1])
        os.chdir(way_to_file)
        openf(name_f)
        percentile(datas)
        median(datas)
        maximum(datas)
        minimum(datas)
        mean(datas)
