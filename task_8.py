# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты
# обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию. Для каждого
# объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий размер файлов в
# ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle

__all__ = ["path_to_files"]


def path_to_files(dir_):
    data_list = []
    folder_size = 0
    for cur_dir, dirs, files in os.walk(dir_, topdown=False):
        for i in files:
            cur_file = cur_dir + "\\" + i
            file_size = os.path.getsize(cur_file)
            folder_size += file_size
            data_list.append({"path": cur_file, "type": "file", "size": file_size})
        data_list.append({"path": cur_dir, "type": "folder", "size": folder_size})
    return data_list


if __name__ == '__main__':
    while True:
        required_dir = input("Введите директорию.\nЕсли желаете использовать текущую директоию, оставьте поле пустым: ")
        if required_dir == "":
            data = path_to_files(os.getcwd())
            break
        elif os.path.isdir(required_dir):
            data = path_to_files(required_dir)
            break
        else:
            print("Вы ввели неправильный путь. Попробуйте снова.")
    with (open('dir_csv.csv', 'w', newline='', encoding='utf-8') as csv_file,
          open('dir_json.json', 'w', encoding='utf-8') as json_file,
          open('dir_pickle.pickle', 'wb') as pickle_file):
        fields = ['path', 'type', 'size']
        writer = csv.DictWriter(csv_file, fields, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
        writer.writeheader()
        writer.writerows(data)
        json.dump(data, json_file)
        pickle.dump(data, pickle_file)
