# 9. Найти максимальный элемент
# среди минимальных элементов столбцов матрицы.

from random import randint

matrix = []

for i in range(4):
    matrix.append([])
    # sum = 0
    for j in range(4):
        number = randint(1, 101)
        # sum += number
        matrix[i].append(number)
    # matrix[i].append(sum)
for i in matrix:
    print(*i)

max_num = -1
for j in range(4):
    min_numb = 100
    for i in range(4):
        if matrix[i][j] < min_numb:
            min_numb = matrix[i][j]
    if min_numb > max_num:
        max_num = min_numb
print("Максимальный среди минимальных: ", max_num)
