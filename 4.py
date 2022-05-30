# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

rand_massive = [randint(1, 5) for _ in range(1, 15)]
print(f'Массив - {rand_massive}')

counter = 0
most = 0

for i in rand_massive:
    f = rand_massive.count(i)
    if f > counter:
        counter = f
        most = i
print(most)


print(f'Число {most}, встречается {rand_massive.count(counter)} раза')
