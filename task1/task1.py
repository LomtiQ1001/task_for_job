import sys
import os
import numpy as np

datas = []

def openf(name_file: str):
    #  сканируем файл и записываем его значения в список в удобном формате
    with open(name_file) as f:
        data = []
        for line in f:
            data.append([float(x) for x in line.split()])
        for i in range(len(data)):
            for j in range(len(data[i])):
                datas.append(data[i][j])

def percentile(lst):
    # узнаём перцентель и выводим
    perc = np.percentile(lst, 90)
    perc = f'{perc:.{2}f}'
    print(perc)

def median (lst):
    # узнаём медиану и выводим
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
    # находим максимум и выводим
    s = sorted(lst)
    max = len(s)
    max = f'{max:.{2}f}'
    print(max)

def minimum (lst):
    # находим минимум и выводим        
    s = sorted(lst)
    min = s[0]
    min = f'{min:.{2}f}'
    print(min)

def mean (lst):
    # находим среднее и выводим
    sum = 0
    i = 0
    for i in range(len(lst)):
        sum += i
    rezult = sum / len(lst)
    rezult = f'{rezult:.{2}f}'
    print(rezult)

# начало программы
if __name__ == "__main__":
    # проверяем есть ли аргументы
    if len (sys.argv) > 1:
        # в случае если файл лежит в отличном от скрипта каталоге, то записываем путь к файлу и имя файла в переменные
        way_to_file = os.path.dirname(sys.argv[1])
        name_f = os.path.basename(sys.argv[1])
        # открыли каталог с файлом        
        os.chdir(way_to_file)
        # запустили функции для обработки
        openf(name_f)
        percentile(datas)
        median(datas)
        maximum(datas)
        minimum(datas)
        mean(datas)
