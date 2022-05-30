# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

our_massive = [randint(1, 30) for _ in range(10)]
print(our_massive)
min_index = our_massive.index(min(our_massive))
max_index = our_massive.index(max(our_massive))
if min_index < max_index:
    print(f'Сумма элементов - {sum(our_massive[min_index+1 : max_index])}')
else:
    print(f'Сумма элементов - {sum(our_massive[max_index+1 : min_index])}')
