"""
Задание 1.
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
# unordered_list = [42, 73, 5, 42, 42, 2, 2, 3, 7, 73, 73, 42] 
# count_frequency = filter(lambda x: unordered_list.count(x) > 1, unordered_list)
# count_frequency = list(set(count_frequency))
# print(sorted(count_frequency))


"""
Задание 2.
В большой текстовой строке подсчитать кол-во встречаемых слов
и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из векипедии или из документации к языку.
"""

# text = 'Python представляет  популярный высокоуровневый язык программирования, который предназначен для создания приложений различных типов. Это и веб-приложения, и игры, и настольные программы, и работа с базами данных. Довольно большое распространение питон получил в области машинного обучения и исследований искусственного интеллекта. Впервые язык Python был анонсирован в 1991 году голландским разработчиком Гвидо Ван Россумом. С тех пор данный язык проделал большой путь развития. В 2000 году была издана версия 2.0, а в 2008 году - версия 3.0. Несмотря на вроде такие большие промежутки между версиями постоянно выходят подверсии. Так, текущей актуальной версией на момент написания данного материала является 3.12, которая вышла в октябре 2023 года.'
# new_text = text.lower().split()
# my_dict = {}
# print(new_text)
# for i in new_text:
#     my_dict[i] = new_text.count(i)
#     (my_dict)
# s_value = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
# for key, item in enumerate(s_value[:10], start=1):
#     print(f'{key} --> {item}')


"""
Задание 3
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один доступный вариант.
"""

# backpak = {'палатка': 12,
#            'вода': 4,
#            'спальник': 6,
#            'аптечка': 2,
#            'еда': 9,
#            'коврик': 1,
#            'одежда': 4,
#            'посуда': 2}

# max_weight = int(input('Введите максимальное вес рюкзака: '))
# lst_items = list()

# for item, weigth in backpak.items():
#     if weigth < max_weight:
#         lst_items.append(item)
#         max_weight -= weigth

# print(*lst_items)





