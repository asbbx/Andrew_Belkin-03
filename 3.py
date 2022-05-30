# 3. В массиве случайных целых чисел
# поменять местами минимальный и максимальный элементы.

from random import randint

r_massive = [randint(1, 51) for _ in range(1, 6)]
print(f'Было - {r_massive}')

min = min(r_massive)
max = max(r_massive)

min_ind = r_massive.index(min)
max_ind = r_massive.index(max)
r_massive[min_ind], r_massive[max_ind] = r_massive[max_ind], r_massive[min_ind]

print(f'Стало - {r_massive}')
