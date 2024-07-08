# Тип № 1.

# region Пример № 1.
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n. Для какого наименьшего неотрицательного целого числа А формула

# x & 29 ≠ 0 → (x & 17 = 0 → x & А ≠ 0)

# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной x)?

# Решение:
'''
def F(x, A):
    return (x&29 != 0) <= ((x&9 == 0) <= (x&A != 0)) # пишем выражения из условия

for A in range(1, 100):
    if all(F(x, A) for x in range(1, 1000)):
        print(A)
'''
# endregion

# Тип № 2.

# region Пример № 2.
# Для какого наибольшего целого числа А формула

# ((x ≤ 9) →(x ⋅ x ≤ A)) ⋀ ((y ⋅ y ≤ A) → (y ≤ 9))

# тождественно истинна, т.е. принимает значение 1 при любых целых неотрицательных x и y?

# Решение:
'''
def F(x, y, A):
    return ((x <= 9) <= ((x*x) <= A)) and (((y*y) <= A) <= (y <= 9)) # пишем выражения из условия

for A in range(1, 100):
    if all(F(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
        print(A)
'''
# endregion

# Тип № 3.

# region Пример № 3.
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наибольшего натурального числа А формула

# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 4))

# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

# Решение:
'''
def F(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0)) # пишем выражения из условия

for A in range(1, 100):
    if all(F(x, A) for x in range(1, 1000)):
        print(A)
'''
# endregion











