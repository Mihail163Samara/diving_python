# data = 0
# while data < 100:
#     data += 3
#     if data % 19 == 0:
#         continue
#     data += 1
#     if data / 40 == 0:
#         break

# else:
#     data += 5
# print(data)



""""
Пользователь вводит число от 1 до 999. Используя операции с числами 
сообщите что введено: цифра, двух или трёхзначное число.
Для 1 цифры верните её квадрат
Для двухзначной цифры число произведения цифр
Для трёх значного чиста ее зеркальное отображение
Если число не из диапазона, запросить новое число от пользователя
Откажитесь от магических чисел
В коде должны быть один input и один print  
"""

# LOWER_LIMIT = 1
# UPPER_LIMIT = 999
# ONE = 1
# TEN = 10
# HUNDRED = 100
# SQRT = 2

# num = LOWER_LIMIT - ONE
# while num < LOWER_LIMIT or num > UPPER_LIMIT:
#      num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT} : '))
# if num < TEN:
#      res = f'{num} - цифра. Её квадрат = {num**SQRT}'
# elif num < HUNDRED:
#      first_num = num//TEN
#      second_num = num%TEN
#      res  = f'Число {num} - двухзначная число. Произведение цифр = {first_num*second_num}'
# else:
#      first_num = num//HUNDRED
#      second_num = num//TEN%TEN
#      third_num = num%TEN
#      mirror = third_num * HUNDRED + second_num * TEN + first_num
#      res = f' Число {num} - трёхзначное число. Его зеркальное число ={mirror}'
# print(res)


# нарисовать в консоли ёлку, спросить у пользователя
# количество рядов. 
# Сколько рядом у ёлки? 3
#                             *
#                            ***
#                           *****
 
# SPACE  = ' '
# START = '*'
# ONE = 1


# вывидите в кнсоль таблицу умножения от 2х2 
# до 9х10 как на школьгой тетраде
# LOWER_LIMIT = 2
# UPPER_LIMIT = 10
# COLUMN = 4
# ONE = 1

# for i_main in (LOWER_LIMIT, LOWER_LIMIT + COLUMN):
#      for s_num in range(LOWER_LIMIT, UPPER_LIMIT + ONE):
#           for  f_num in range(i_main, i_main + COLUMN):
#                print(f'{f_num: > 3} Х {s_num: > 3} = {f_num * s_num: > 3}' ,  end = ' \t ' )
#           print()
#      print()
            

# for one in (2,6) :         
#       for i in range(2, 10):
#           for j in range(2,10):
#                print(j, '*', i, '=' ,i*j, end = '\t')
#           print()
               
# num = float(input("введите число : "))
# f=' '
# i = 0
# while i <= num:
#     print(f'{f}*{i} - kjv')
#     f+=' '
#     i+=5
    

# num = float(input("введите число : "))
# f=' '
# i = 0
# while i < num:
#     f+=' '
#     i+=5
#     if i == 35:
#         continue
#     print(f'{f}*{i} - kjv')


# num = float(input('Введите число: '))
# STEP = 2
# limit = num - STEP
# count = -STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue
#     print(count)

# min_limit = 0
# max_limit = 10
# while True:
#     print('Введи число между', min_limit, 'и', max_limit, '? ')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
# print('Было введено число ' + str(num))


# min_limit = 0
# max_limit = 10
# count = 3

# while count > 0:
#     print('Попытка ' + str(count))
#     count -= 1

#     num = float(input('Введи число между ' + str(min_limit) + ' и ' + str(max_limit) + ': '))
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break

# else:
#     print('Исчерпаны все попытки. Сожалею.')
#     quit()

# print('Было введено число ' + str(num))


# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#     print(f'{item} + {str('pis')}')


# num = int(input('Введите число: '))
# for i in range(10, num, -2):
#     print(i)

# count = 10

# for i in range(count):
#     for j in range(count):
#         for k in range(count):
#             for s in range(count):
#                 print(i, j, k, s)


# count = 10
# for i in range(count):
#     print(i)
# for i in range(count):
#     print(i)

# animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
# for i, animal in enumerate(animals, start=1):
#     print(i,animal)

'''Важно! Функция enumerate позволяет перебирать только целые числа в
порядке возрастания с шагом один.
----------------------------------------------------------'''

# data = 0
# while data < 100:
#     data += 2
#     if data % 40 == 0:
#         break
# print(data)

# data = 0
# while data < 100:
#     data += 3
#     if data % 40 == 0:
#         break
# else:
#     data += 5
# print(data)


# data = 0
# while data < 100:
#     data += 3
#     if data % 19 == 0:
#         continue
#     data += 1
#     if data % 40 == 0:
#         break
# else:
#     data += 5
# print(data)

# num = 40 % 40
# print(num)




# import sys

# num = int(input('Введите число :'))
# print(num, type(num), id(num), sys.getsizeof(num), sep=', ')


# print(dir(int))


# txt = (input(' Введи число или текс или всё в месте : '))
# if txt.isnumeric():
#     print(bin(int(txt)), oct(int(txt)), hex(int(txt)), sep='\n')
# else:
#     print(f'здесь присутсвуют буквы {txt}')
#     print(txt.isascii())

# x = 42
# y = 'text'
# z = 3.1415
# print(hash(x), hash(y), hash(z))
# my_list = [x, y, z]
# print(hash(my_list)) # получим ошибку, т.к. list изменяемый


# a: typing  = 42
# b: float = float(input('Введи число: '))
# a = a / b
# print(a)

# print("Hello world!".__doc__)
# print(str.__doc__)


# s = 45
# print(help(s))

# print(help(str))
# quit

# a = 'Привет, ты любишь кока-колу'
# print(keywords)

# x = int("42")
# y = int(3.1415)
# z = int("hello", base=30)
# print(x, y, z, sep='\n')

# import sys

# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP


# num = 2 ** 16 - 1
# b = bin(num)
# o = oct(num)
# 17
# h = hex(num)
# print(b, o, h)


# DEFAULT = 42
# num = int(input('Введите уровень или ноль для значения по умолчанию: '))
# level = num or DEFAULT
# print(level)

# name = input('Как вас зовут? ')
# if name:
#     print('Привет, ' + name)
# else:
#     print('Анонимус, приветствую')


# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for i in enumerate(data, start=1):
#     print(i)
    
# LIMIT = 120
# ATTENTION = 'Внимание!'
# 21
# name = input('Твоё имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
# " до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
# print(text)

# empty_str = ''
# en_str = 'Text'
# ru_str = 'Текст'
# unicode_str = '😀😍😉🙃'
# print(empty_str.__sizeof__())
# print(en_str.__sizeof__())
# print(ru_str.__sizeof__())
# print(unicode_str)

import math
import decimal
import fractions


# pi = decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_88\
# 4_197_169_399_375')
# print(pi)
# num = decimal.Decimal(1) / decimal.Decimal(3)
# print(num)


# decimal.getcontext().prec = 120
# science = 2 * pi * decimal.Decimal(23.452346) ** 2
# print(science)

# f1 = fractions.Fraction(1, 3)
# print(f1)
# f2 = fractions.Fraction(3, 5)
# print(f2)
# print(f1 * f2)


# a = complex(2, 3)
# b = complex('2+3j')
# print(a, b, a == b, sep='\n')

# a = 500
# b = 3
# print(divmod(a, b))
# print(pow(a,b, 7))