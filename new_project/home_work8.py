"""
Задание 2. 
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все
вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом
всех вложенных файлов и директорий.
"""

import os
import json
import csv
import pickle

from pathlib import Path


def walker_directory(file: Path) -> None:
    result = []
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        for name in file_name:
            result.append({
                'parent_directory': dir_path,
                'type': 'File' if ('.' in name) or (len(name.split('.')) == 2) else 'Directory',
                'name': name,
                'size_bytes': os.path.getsize(os.path.join(dir_path, name))

            })
    with open(r'C:\python_diving\new_project\result.json',
              'w') as json_file:
        json.dump(result, json_file, ensure_ascii=False)

    with open(r'C:\python_diving\new_project\result.csv',
              'w', newline='', encoding='utf-8') as csv_file:
        writer_csv = csv.DictWriter(csv_file, fieldnames=result[0].keys())
        writer_csv.writeheader()
        writer_csv.writerows(result)

    with open(r'C:\python_diving\new_project\result.pickle',
              'wb') as pickle_file:
        pickle.dump(result, pickle_file)


if __name__ == '__main__':
    os.chdir('..')
    walker_directory(Path.cwd())