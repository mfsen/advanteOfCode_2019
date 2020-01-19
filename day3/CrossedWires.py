import numpy as np

f = open("input.txt")
paths = f.readlines()
arrayofcommads1 = paths[0].split(",")
arrayofcommads2 = paths[1].split(",")

array = np.zeros((10000,10000))
index1 = 5000
index2 = 5000
for i in arrayofcommads1:
    num= int(i[1:])
    if i[0] == 'R':
        temp = index2 + num
        array[index1][index2:temp] +=1
        index2=temp
    if i[1] == 'D':
        temp = index1 + num
        array[index1:temp][index2] +=1
        index1=temp
    if i[1] == 'L':
        temp = index2 - num
        array[index1][index2:temp] +=1
        index2=temp
    if i[1] == 'U':
        temp = index1 - num
        array[index1:temp][index2] +=1
        index1=temp

for i in arrayofcommads2:
    num= int(i[1:])
    if i[0] == 'R':
        temp = index2 + num
        array[index1][index2:temp] +=1
        index2=temp
    if i[1] == 'D':
        temp = index1 + num
        array[index1:temp][index2] +=1
        index1=temp
    if i[1] == 'L':
        temp = index2 - num
        array[index1][index2:temp] +=1
        index2=temp
    if i[1] == 'U':
        temp = index1 - num
        array[index1:temp][index2] +=1
        index1=temp

print("ok1")
corressd=[]
for s in range(len(array)):
    for d in range(len(array[0])):
        if array[s][d] == 2:
            corressd.append([s,d])

print(corressd)
print("ok2")