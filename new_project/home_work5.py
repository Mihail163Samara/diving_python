"""
Задание 2. 
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

# def path_to_file(txt: str):
#     *path, other = txt.split("/")
#     name, ext = other.split(".")
#     return path, name, ext


# link = 'C:\python_diving\new_project\home_work5.py'

# result = path_to_file(link)

# print(f'path = {",".join(result[0])}\nname = {result[1]}\next = {result[2]}')


"""
Задание 3. 
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int,
премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""

# import decimal

# n = ['Sergey', 'Nikita', 'Michail']
# b = [10_000, 20_000, 17_000]
# r = ['25.25%', '10.14%', '14.5%']

# dct = {name: round(bets * ((decimal.Decimal(reward.replace('%', ''))) / 100), 2) + bets for name, bets, reward in
#        zip(n, b, r)}

# print(dct)


"""
Задание 4. 
Создайте функцию генератор чисел Фибоначчи
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
"""

def fibonacci(n: int):
    if n == 0:
        yield 0
    elif n == 1:
        yield 1
    else:
        f1, f2 = 0, 1
        for _ in range(n):
            yield f1
            f1, f2 = f2, f1 + f2

result = fibonacci(10)
print(*result)