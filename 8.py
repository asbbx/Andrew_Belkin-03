# 8. Матрица 5x4 заполняется вводом с клавиатуры
# кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    matrix.append([])
    sum = 0
    for j in range(4):
        number = int(input(f'Введите матрицу, строка - {i+1}, '
                           f'элемент - {j+1}: '))
        sum += number
        matrix[i].append(number)
    matrix[i].append(sum)
for i in matrix:
    print(*i)