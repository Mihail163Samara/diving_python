# a = 12
# b = 'Hallo!'
# c = 3.14
# d = True

# print(f'{type(a) = }')
# print(f'{type(b) = }')
# print(f'{type(c) = }')
# print(f'{type(d) = }')

"""
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок . Для каждого элемнта в цикле выведите:
порядковый номер начиная с единици
значение
адрес в памяти
размер в памяти
хэш объекта
результат проверки на целое число только если он положительный
результат проверки на строку только если он положительный
добавте в список повторяющиеся элементы и сравните результаты

"""
# import sys


# data = [42, 73.0, 'Hello world!' , True, 42, 'Hello world!' , 256,  2 ** 8, 1, 'Привет, мир! ' ]

# for nn, value in enumerate(data, start=1 ):
#     chek_int = 'Похоже на целое число' if isinstance(value, int) else ''
#     chek_str = 'Похоже на строку' if isinstance(value, str) else ''
#     print(f'\n{nn}) Объект {value}\nАдрес в памяти {id(value)}\nРазмер в памяти {sys.getsizeof(value)}\nХэш объекта {hash(value)}\n{chek_int}{chek_str} \n')



"""
Напишите программу которая получает целое число и возвращает его двоичное, восьмеричное строкомое представление.
Функции bin и oct используйте для проверки своего результата, а не для решения.
Дополнительно: 
Попробуйте избежать дублирование кода в преобразование к разным системам счисления.
Избегайте магических чисел.
Добавте аннотацию типов где это возможно.

"""
# BIN = 2
# OCT = 8


# num = int(input('Введите число :'))


# for div in(BIN, OCT):
#     test_num: int = num 
#     result: str = ''
#     while test_num > 0:
#         result = str(test_num % div) + result
#         test_num //=div

#     print(f'{div=} {result=}')
# print(f'{bin(num)} {oct(num)}')


"""
Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
Диаметр не привышвет 1000 у.е.
Точность вычисления должна составлять не мение 42 знаков после запятой.

"""

# import math
# import decimal

# decimal.getcontext().prec = 50
# PI = decimal.Decimal(math.pi)

# d = decimal.Decimal(input('Введите диаметр окружности : '))
# while d > 1000:
#     print('Некорректный ввод : ')
#     d = decimal.Decimal(input('Введите диаметр окружности : '))

# print(f'Площадь круга : {PI*(d/2)**2}\nДлина окружности : {PI*d}')


"""
Напишите программу которая решает квадратные уравнения даже если дискреминант отрицательный.
Используйте комплексные числа для извлечения квадратного корня.

"""

# a = float(input('Введите коэффициент a = '))
# b = float(input('Введите коэффициент b = '))
# c = float(input('Введите коэффициент c = '))

# d = b ** 2 - 4 * a * c
# if d > 0:
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     result = f'У уравнения два корня :\n{x1=}\n{x2=}'
# elif d == 0:
#     x1 = -b / (2*a)
#     result = f'У уравнения один корня :\n{x1=}'
# else:
#     d = complex(d,0)
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     result = f'У уравнения два комлексных корня :\n{round(x1.real, 2)+round(x1.imag, 2) * 1j}\n{round(x2.real, 2)+round(x2.imag, 2) * 1j}'
# print(result)


"""
Напишите программу банкомата.
Начальная сумма равна нулю
Допустимые действия пополнить, снять, выйти
Сумма пополнения и снятия кратна 50 у.е.
процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляються проценты - 3%
Нельзя снять больше, чем на счёте
При привешении суммы в 5 млн, вычитать налог  на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег 
"""

# import decimal

# CMD_DEPOSIT = 'п'
# CMD_WITHDRAW = 'с'
# CMD_EXIT = 'в'
# RICHNESS_SUM = decimal.Decimal(5_000_000)
# RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
# WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
# ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
# MULTIPLICITY = 50
# MIN_REMOVAL = 30
# MAX_REMOVAL = 600
# COUNT_OPER = 3

# # decimal.getcontext().prec = 2
# account = decimal.Decimal(0)
# count = 0

# while True:
#     command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}" ')
#     if command == CMD_EXIT:
#         print(f'Заберите вашу карту.\nНа вашем счёте {account} у.е.')
#         break
#     if account > RICHNESS_SUM:
#         percent = account * RICHNESS_TAX
#         account -= percent
#         print(f'Удержан налог на богатство {RICHNESS_TAX}% в размере {percent} у.е.\nИтого на карте осталось {account} у.е.')
#     if command in (CMD_DEPOSIT, CMD_WITHDRAW):
#         ammount = 1
#         while ammount % 50 != 0:
#             ammount = int(input(f'Введите сумму, кратную {MULTIPLICITY} у.е.'))
#     if command == CMD_DEPOSIT:
#         account += ammount
#         count+=1
#         print(f'Пополнение карты на {ammount} у.е.\nИтого на карте {account} у.е. ')
#     elif command == CMD_WITHDRAW:
#         withdraw_tax = ammount * WITHDRAW_PERCENT
#         withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else 
#                                   MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
#         if account >= ammount + withdraw_tax:
#             count +=1
#             account -= (ammount + withdraw_tax)
#             print(f'Снятие с карты {ammount} у.е.\nКомисия за снитие {withdraw_tax}\nНа карте осталось {ammount} у.е.')
#         else:
#             print(f'Недостаточно для снятия\nСумма снятия {ammount + withdraw_tax} у.е.\nКомиссия {withdraw_tax} у.е.\nНа вашей карте {account} у.е.')
#     if count and count % COUNT_OPER == 0:
#         bonus_percent = account * ADD_PERCENT
#         account += bonus_percent
#         print(f'На ваш счёт начисленно {ADD_PERCENT}%\nCоставляющие{bonus_percent} у.е.\nИ того на вашем счёте{account}у.е.')