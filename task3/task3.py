import sys
import os

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data = [data1, data2, data3, data4, data5]
text = ["Cash1.txt", "Cash2.txt", "Cash3.txt", "Cash4.txt", "Cash5.txt"]

def openf(txt_files):
    # сканировали файлы и записали данные
    datas1 = []
    datas2 = []
    datas3 = []
    datas4 = []
    datas5 = []
    datas = [datas1, datas2, datas3, datas4, datas5]
    for i in range(len(txt_files)):
        with open(txt_files[i]) as f:
            for line in f:
                datas[i].append([float(x) for x in line.split()])
            for j in range(len(datas[i])):
                for k in range(len(datas[i][j])):
                    data[i].append(datas[i][j][k])

def find_max():
    # нашли максимальое значение и вывели его индекс + 1, что будет равно искомому интервалу с наибольшим количеством посетителей
    final = []
    for i in range(len(data1)):
        final.append(data1[i] + data2[i] + data2[i] + data2[i] + data2[i])
    rezult = max(final)
    for i in range(len(data1)):
        if rezult == final[i]:
            print(i+1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # переходим в дирректорию с файлами
        os.chdir(sys.argv[1])
        # с помощью функций обрабатываем файлы и находим ответ на поставленную задачу
        openf(text)
        find_max()
