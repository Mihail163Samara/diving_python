"""
Задание 2. 
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""
# def _is_not_leap(year: int) -> bool:
#     return not (year % 400 == 0 or year % 100 != 0 and year % 4 == 0)


# def check_date(full_date: str) -> bool:
#     day, month, year = (int(item) for item in full_date.split('.'))
#     if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
#         return False
#     if month in (4, 6, 9, 11) and day > 30:
#         return False
#     elif month == 2 and day > 29:
#         return False
#     elif month == 2 and day > 28 and _is_not_leap(year):
#         return False
#     else:
#         return True


# if __name__ == '__main__':
#     print(check_date('10.09.2024'))


"""
Задание 3. 
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""
# def chess_queen(corr_x: list, corr_y: list) -> bool:
#     flag = True
#     for i in range(n):
#         for j in range(i + 1, n):
#             if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
#                 flag = False
#         if flag:
#             return True
#         return False


# n = 8
# x = list()
# y = list()
# for i in range(n):
#     new_x, new_y = [int(i) for i in input().split()]
#     x.append(new_x)
#     y.append(new_y)

# print(chess_queen(x, y))


"""
Задание 4. 
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в
задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
import random

n = 8
count = 0
dct = dict()

def chess_queen(corr_x: list, corr_y: list) -> bool:
    flag = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                flag = False
        if flag:
            return True
        return False


while True:
    x = list()
    y = list()
    for i in range(n):
        new_x, new_y = random.sample(list(range(1, 9)), k=2)
        x.append(new_x)
        y.append(new_y)
    if chess_queen(x, y):
        lst = [list(i) for i in zip(x, y)]
        dct[count + 1] = lst
        count += 1
        print(f"комбинация №{count} подобрана")
    if count == 4:
        break

for k, v in dct.items():
    print(f"Комбинация №{k}, с координатами ферзя: {v}")