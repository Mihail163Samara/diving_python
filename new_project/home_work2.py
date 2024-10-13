"""
Урок 2. Простые типы данных.

1. Решить задачи, которые не успели решить на семинаре.
"""


"""
2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйте для проверки своего результата.
"""

# HEX = 16

# num = int(input('Введите число :'))

# test_num: int = num 
# result: str = ''
# while test_num > 0:
#     result = str(test_num % HEX) + result
#     test_num //=HEX

# print(f'\n{HEX=} {result=}')

# print(f'\nПроверка результата: {hex(num)}\n')

"""
3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
"""
# import fractions

# first: str = str(input("Введите числитель первой дроби "))
# second: str = str(input("Введите знаменатель первой дроби "))
# third: str = str(input("Введите числитель второй дроби "))
# fourth: str = str(input("Введите знаменатель второй дроби "))
# number1: int = int(first)
# number2: int = int(second)
# number3: int = int(third)
# number4: int = int(fourth)


# result1 = (number1 / number2 ) + (number3 / number4)
# result2 = (number1 / number2 ) * (number3 / number4)
# print(result1)
# print(result2)
# firstfraction = fractions.Fraction(number1, number2)
# secondfraction = fractions.Fraction(number3, number4)
# result3 = firstfraction + secondfraction
# result4 = firstfraction * secondfraction
# print(result3)
# print(result4)
