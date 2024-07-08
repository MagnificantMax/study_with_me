# region Пример № 1.

# В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от −10000 до 10000 включительно.
# Определите и запишите в ответе сначала количество пар элементов последовательности, в которых хотя бы одно число делится на 3,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

# Решение:
'''
count = 0
maxi = 0
f = open('17.txt').readlines()
M = [int(i) for i in f]

for i in range(len(M) - 1): # пробегаем по парам, состоящие из последовательных чисел
    if M[i] % 3 == 0 or M[i+1] % 3 == 0: # если хотя бы одно число делится на 3
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# endregion

# region Пример № 2.

# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, у которых разность элементов кратна 36
# и хотя бы один из элементов кратен 13, затем максимальную из разностей элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

# Решение:

'''
from itertools import *

count = 0
maxi = 0
f = open('17.txt').readlines()
M = [int(i) for i in f]


for i in combinations(M, 2): # пробегаем по различным парам в файле
    if (i[0] - i[1]) % 36 == 0 and (i[0] % 13 == 0 or i[1] % 13 == 0):
        count += 1
        maxi = max(maxi, i[0] - i[1])
print(count, maxi)
'''
# endregion

# region Пример № 3.

# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
# Назовём тройкой три идущих подряд элемента последовательности.
# Определите количество троек чисел таких, которые могут являться сторонами прямоугольного треугольника.
# В ответе запишите два числа: сначала количество найденных троек, а затем — максимальную сумму элементов таких троек.
# Если таких троек не найдётся — следует вывести 00.

# Решение:
'''
count = 0
maxi = 0
f = open('17.txt').readlines()
M = [int(i) for i in f]

for i in range(0, len(M) - 2): # пробегаем по тройкам, состоящие из последовательных чисел
    A = [M[i], M[i + 1], M[i + 2]]
    A.sort()
    if A[2] ** 2 == (A[0] ** 2 + A[1] ** 2):
        count += 1
        maxi = max(maxi, A[0] + A[1] + A[2])

print(count, maxi)
'''
# endregion


M = [int(x) for x in open('files/17.txt')]
print(M)
























































































































