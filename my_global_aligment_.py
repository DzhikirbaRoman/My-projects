"""
import numpy as np

a = np.arange(10, 19).reshape((3, 3))
print(a)
c = a[[0,2], 0:2]
print("\n \n")
print(c)
def foo(x):
   return x/2
f1 = np.apply_along_axis(foo, axis=1, arr=a)
f2 = np.apply_along_axis(foo, axis=0, arr=a)
print(f1," \n \n")
print(f2)
a1 = a[a > 14]
print(a1)
fa = np.random.random(12)
fa = fa.reshape(3, 4)
print(fa)
[a4,a5,a6] = np.split(a,[1,3],axis=1)
print(a4," \n",a5, "\n" ,a6)
"""
print("Для коректної роботи програми вводьте будь ласка лише англійські літери ")
horizontal = input("Введіть будь ласка першу генетичну послідовність з великих англійських літер , наприклад  'ATCGTTAGCT'   : ")
vertical = input("Введіть будь ласка другу генетичну послідовність з великих англійських літер , наприклад  'ATCAGTGTAGCT' : ")

horizontal = horizontal.upper()
vertical = vertical.upper()

match = 1
missmatch = -1
gap = -2
matrix = []
for h in horizontal:
    if (h != "A") and (h != "T") and (h != "G") and (h != "C"):
        print("Ви ввели некоректну генетичну послідовність ")
        break


for h in vertical:
    if (h != "A") and (h != "T") and (h != "G") and (h != "C"):
        print("Ви ввели некоректну генетичну послідовність ")
        break

for i in range((len(vertical) + 2)):
    matrix.append([0] * (len(horizontal) + 2))

for i in range((len(vertical)+1)):
    matrix[i+1][1] = gap * i
for j in range((len(horizontal)+1)):
    matrix[1][j+1] = gap * j
l2 = 1
for h in horizontal:
    l2 += 1
    matrix[0][l2] = h
l1 = 1
for h in vertical:
    l1 += 1
    matrix[l1][0] = h

for i in range(2, (len(horizontal) + 2)):
    for j in range(2, (len(vertical) + 2)):
        if matrix[j][0] == matrix[0][i]:
            position1 = matrix[j - 1][i - 1] + match
        else:
            position1 = matrix[j - 1][i - 1] + missmatch

        position2 = matrix[j - 1][i] + gap
        position3 = matrix[j][i - 1] + gap

        position = max(position1, position2, position3)
        matrix[j][i] = position

matrixR = []
for i in range(3):
    matrixR.append([])

i1 = 0
j1 = 0
lv = len(horizontal) + 1
lh = len(vertical) + 1
pl = 0
matrix[1][1] = int(matrix[1][1])
while (lv - 2 >= i1) and (lh - 2 >= j1):

    if (lv - 2 >= i1) and (lh - 2 >= j1) and (matrix[lh - j1][lv - i1] == matrix[lh - j1 - 1][lv - i1 - 1] + match) and (
            matrix[lh - j1][0] == matrix[0][lv - i1]):
        lh1 = matrix[lh - j1][0]
        lv1 = matrix[0][lv - i1]
        matrixR[0].append(lh1)
        matrixR[1].append(lv1)
        j1 += 1
        i1 += 1
    elif (lv - 2 >= i1) and (lh - 2 >= j1) and (matrix[lh - j1][lv - i1] == matrix[lh - j1 - 1][lv - i1 - 1] + missmatch) and (
            matrix[lh - j1][0] != matrix[0][lv - i1]):
        lh1 = matrix[lh - j1][0]
        lv1 = matrix[0][lv - i1]
        matrixR[0].append(lh1)
        matrixR[1].append(lv1)
        j1 += 1
        i1 += 1
    else:
        if (lh - 2 >= j1) and (matrix[lh - j1][lv - i1] == matrix[lh - j1 - 1][lv - i1] + gap):
            lh1 = matrix[lh - j1][0]
            matrixR[0].append(lh1)
            matrixR[1].append("_")
            j1 += 1

        else:
            lv1 = matrix[0][lv - i1]
            matrixR[0].append("_")
            matrixR[1].append(lv1)
            i1 += 1



mr3 = len(matrixR[0])
for i in range(len(matrixR[0])):
    if matrixR[0][mr3 - 1 - i] == matrixR[1][mr3 - 1 - i]:
        matrixR[2].append(1)
    elif (matrixR[0][mr3 - 1 - i] == "_") or (matrixR[1][mr3 - 1 - i] == "_"):
        matrixR[2].append(-2)
    elif matrixR[0][mr3 - 1 - i] != matrixR[1][mr3 - 1 - i]:
        matrixR[2].append(-1)
matrixR[0] = matrixR[0][::-1]
matrixR[1] = matrixR[1][::-1]
for i in range(len(horizontal) + 2):
    for j in range(len(vertical) + 2):
        if len(str(matrix[j][i])) < 2:
            matrix[j][i] = '  ' + str(matrix[j][i]) + "  "
        elif 2 <= len(str(matrix[j][i])) < 3:
            matrix[j][i] = ' ' + str(matrix[j][i]) + "  "
        elif 3 <= len(str(matrix[j][i])) < 4:
            matrix[j][i] = '' + str(matrix[j][i]) + "  "
sum1 = 1
sum2 = 1
for i in range(mr3):
    sum1 = matrixR[2][i]
    sum2 += sum1
for j in range(3):
    for i in range(mr3):
        if len(str(matrixR[j][i])) < 2:
            matrixR[j][i] = '  ' + str(matrixR[j][i]) + "  "
        elif 2 <= len(str(matrixR[j][i])) < 3:
            matrixR[j][i] = ' ' + str(matrixR[j][i]) + "  "
        elif 3 <= len(str(matrixR[j][i])) < 4:
            matrixR[j][i] = '' + str(matrixR[j][i]) + "  "
for i in range(len(matrix)):
    print(*matrix[i])
print(" \n \n \n")
print(" Зворотній шлях :")
for i in range(len(matrixR)):
    print(*matrixR[i])
print("Сума матриці: ", sum2-1)