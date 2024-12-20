
# region 📚 Шпаргалка ЕГЭ | Задание №12

# Задание №1:
# Дана программа для Редактора:
#
# НАЧАЛО
#    ПОКА нашлось (11)
#       заменить (112, 4)
#       заменить (113, 2)
#       заменить (42, 3)
#       заменить (43, 1)
#    КОНЕЦ ПОКА
# КОНЕЦ
# Какая строка получится в результате применения приведённой программы к строке
# вида 1…13…32…2 (170 единиц, 100 троек и 7 двоек)?

# Решение:
'''
s = 170 * '1' + 100 * '3' + 7 * '2'

while '11' in s:
    s = s.replace('112', '4', 1)
    s = s.replace('113', '2', 1)
    s = s.replace('42', '3', 1)
    s = s.replace('43', '1', 1)

print(s)
'''


# Задание №2:
# Дана программа для Редактора:
#
# НАЧАЛО
#    ПОКА нашлось (333) ИЛИ нашлось (555)
#       ЕСЛИ нашлось (555)
#          ТО заменить (555, 3)
#          ИНАЧЕ заменить (333, 5)
#       КОНЕЦ ЕСЛИ
#    КОНЕЦ ПОКА
# КОНЕЦ
# На вход приведённой выше программе поступает строка, начинающаяся с цифры «3»,
# а затем содержащая n цифр «5» (3 <n< 10000).
#
# Определите наибольшее возможное значение суммы числовых значений цифр в строке,
# которая может быть результатом выполнения программы.

# Решение:
'''
M = []
for n in range(3, 10000):
    s = '3' + '5' * n
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)

    sum_digits = [int(i) for i in s]
    M.append(sum(sum_digits))

print(max(M))
'''


# Задание №3:
# Дана программа для Редактора:
#
# НАЧАЛО
# ПОКА нашлось (52) ИЛИ нашлось (2222) ИЛИ нашлось (1122)
#    ЕСЛИ нашлось (52)
#      ТО заменить (52, 11)
#    КОНЕЦ ЕСЛИ
#    ЕСЛИ нашлось (2222)
#      ТО заменить (2222, 5)
#    КОНЕЦ ЕСЛИ
#    ЕСЛИ нашлось (1122)
#      ТО заменить (1122, 25)
#    КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ
# На вход приведённой выше программе поступает строка, начинающаяся с цифры «5»,
# а затем содержащая n цифр «2» (3 < n < 10 000).
#
# Определите наименьшее значение n, при котором сумма цифр в строке,
# получившейся в результате выполнения программы, оканчивается на 7.

# Решение:
'''
for n in range(4, 10000):
    s = '5' + '2' * n
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s:
            s = s.replace('52', '11', 1)
        elif '2222' in s:
            s = s.replace('2222', '5', 1)
        elif '1122' in s:
            s = s.replace('1122', '25', 1)

    sum_digits = sum([int(i) for i in s])

    if str(sum_digits)[-1] == '7':
        print(n)
        break
'''


# Задание №4:
# Дана программа для Редактора:
#
# НАЧАЛО
#    ПОКА нашлось(>1) ИЛИ нашлось(>2) ИЛИ нашлось(>3)
#       ЕСЛИ нашлось(>1)
#          ТО заменить(>1, 22>3)
#       КОНЕЦ ЕСЛИ
#       ЕСЛИ нашлось(>2)
#          ТО заменить(>2, 2>)
#       КОНЕЦ ЕСЛИ
#       ЕСЛИ нашлось(>3)
#          ТО заменить(>3, 11>2)
#       КОНЕЦ ЕСЛИ
#    КОНЕЦ ПОКА
# КОНЕЦ
#
# На вход приведённой выше программы поступает строка, начинающаяся с символа «>»,
# а затем содержащая n цифр 1, n цифр 2 и n цифр 3 (3 ≤ n ≤ 50),
# расположенных в произвольном порядке.
# Определите количество значений n, при котором сумма числовых значений цифр строки,
# получившейся в результате выполнения программы кратна 7.

# Решение:
'''
count = 0

for n in range(3, 50 + 1):
    s = '>' + '1' * n + '2' * n + '3' * n
    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>3', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>2', 1)

    sum_digits = sum([int(i) for i in s if i.isdigit()])

    if sum_digits % 7 == 0:
        count += 1

print(count)
'''


# 📚 Полезные ссылки на статьи и разборы задач:
# 📘 Полная версия шпаргалки доступна в нашем тг канале: https://t.me/informatika_kege_itpy/362?comment=1424
# 📘 Разборы 12 номеров по информатике: https://t.me/informatika_kege_itpy/360?comment=1532
# 💡 Генераторы списков (списочные выражения) для ЕГЭ: https://t.me/informatika_kege_itpy/339
# 🐍 Шпаргалка по генераторам списков: https://t.me/informatika_kege_itpy/495
# 💡 Что такое строки (str) в Python и зачем они нужны: https://t.me/informatika_kege_itpy/265
# endregion (не удаляйте меня, я тут не просто так)


# todo: сюда можно писать заметки, чтобы не забыть задать вопрос репетитору ☝️
progress_result = ()  # Сюда заносятся номера, прорешанных задач.
print('Рекомендуемое кол-во решенных задач для закрепления номера 30.')
print(f'Проверим прогресс: ~{int(len(progress_result) * (100 / 30))}% задач прорешано.')
print('aaaa')