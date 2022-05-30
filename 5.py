# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import randint

our_massive = [randint(-5, 21) for _ in range(16)]
print(our_massive)

max_negative = min(our_massive)
pos_max_negative = our_massive.index(max_negative) + 1
print(f'Число - "{max_negative}" , позиция - "{pos_max_negative}"')
