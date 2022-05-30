# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными),
# так и различаться.

from random import randint

our_massive = [randint(1, 101) for _ in range(10)]
print(f'Массив - {our_massive}')

sort_list = []
sort_list.extend(our_massive)
sort_list.sort()
print(f'Два наименьших числа - {sort_list[0]} и {sort_list[1]}.')
