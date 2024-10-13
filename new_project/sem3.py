"""
Задание 1
Вручную создайте список с целыми числами, которые повторяются.
Получите новы список, который содержит уникальные (без повторов) элементы исходного списка.
"""

"""
Подготовте два решения короткое и длиное, которое не использует другие коллекции по мимо списка
"""
# data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42] 
# my_set =list(set(data))
# print(my_set)


# new_list = []
# for i in data:
#     if i not in new_list:
#         new_list.append(i)

# print(new_list)


"""
Пользователь вводит данные. Сделайте проверку данных и преобразуйте в один из вариантов ниже:
1) Целое положительное число 
2) Вещественное положительное или отрицательное число 
3) Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
4) Строку в нижнем регистре в остальных случаях
"""
# data = input('Введите данные: ')
# if data.isdigit():
#     new_data = int(data)
# elif data.count('.') == 1  and data.count('-') < 2 and '-' not in data[1:]  and data.replace('.','').replace('-', '').isdigit():
#     new_data = float(data)
# elif not data.islower():
#     new_data = data.lower()
# else:
#     new_data = data.upper()

# print([new_data])

"""
Создайте вручную кортеж из элементов разного типа.
Получите из него словарь списков, где:
ключ - тип элемента,
значение - список элементов данного типа. 
"""
    
# data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False )
# my_dict = {}
# for item in data:
#     key = my_dict.setdefault(type(item), [])
#     key.append(item)

# print(my_dict)


"""
Задание 4.

1) Создайте вручную список с повторяющимися элементами.
2) Удалите из него все элементы, которые встречаются дважды. 
"""
# COUNT  = 2

# data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42] 

# for i in data:
#     if data.count(i) == COUNT:
#         for _ in range(COUNT):
#             data.remove(i)

# print(data)


"""
Создайте вручную список с повторяющимися целыми числами. 
Сформируйте список с порядкомыми номерами нечётных элементов исходного списка.
Нумерация начинаеться с единици.
"""

# data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42] 

# my_list = []
# for i, values in enumerate(data, 1):
#     if values % 2 != 0:
#         my_list.append(i)
 

# print(f'{data = }')
# print(f'{my_list = }')

"""
Задача 6
Пользователь вводит строку текста. Выведите каждое слово с новой строки .
Строки нумеруються начиная с единицы .
Слова выводятся отсортированными согласно сортировки Unicode .
Текст выравнивается по правому краю так, чтобы у самого длиннго слова был один пробел между ним и номером строки .
"""
# text = sorted(input(' Введите ваш текст: ').split())
# max_len = 0
# for i in text:
#     if len(i) > max_len:
#         max_len = len(i)

# for key, value in enumerate(text, 1):
#     print(f'{key}. {value:>{max_len}}')


"""
Задача 7
Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
Результат сохраните в словаре, где ключ - символ, а значение - частота встечи символа в строке.
обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.
"""

# text = input('Введите ваш текст : ')
# my_dict = {}
# my_dict_1 = {}
# my_dict_2 = {}

# """вариант 1"""

# for i in set(text):
#      my_dict[i] = text.count(i)

# print(f'{my_dict} ')

"""вариант 2"""

# for i in text:
#     if i not in my_dict_1:
#           my_dict_1[i] = 1
#     else:
#          my_dict_1[i] += 1

# print(my_dict_1)

"""вариант 3"""

# for i in text:
#     my_dict_2[i]  = my_dict_2.get(i, 0) + 1

# print(my_dict_2)

"""
Задание 8
Три друга взяли вещи в поход. Сформулируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
1) Какие вещи взяли все три друга.
2) Какие вещи уникальны, есть только у одного друга.
3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует. 
4) Для решения используйте операции с множествами. Код должен расширяться на любое количество друзей.
"""
# hike = {
#      'Aaz' : ("спички", "спальник", "дрова", "топор"),
#      'Skeeva' : ("спальник", "спички", "вода", "еда"),
#      'Tananda' : ("вода", "спички", "косметика"),
# }

# all_things  = set()
# for things in hike.values():
#     # # вариант 1:
#     # for thing in set(things):
#     #     all_things.add(thing)
#     ##вариант 2:
#     all_things.update(things)

# print(f'Полный список вещей {all_things} ')

# unique_things = {}
# for master_friend, master_things in hike.items():
#     for slave_friend, slave_thinhs in hike.items():
#         if master_friend != slave_friend:
#             if master_friend not in unique_things:
#                 unique_things[master_friend] = set(master_things) - set(slave_thinhs)
#             else:
#                 unique_things[master_friend]  -= set(slave_thinhs)

# print(f'Список уникальных вещей {unique_things}')

# double_things = set(all_things)
# for things in unique_things.values():
#     double_things -= things

# print(f'Список дублирующих вещей {double_things}')

# for friend, things in hike.items():
#     print(f'{friend} отсутствует {double_things - set(things)} ')
