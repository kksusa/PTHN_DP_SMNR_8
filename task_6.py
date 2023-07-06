# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестирования
# возьмите pickle версию файла из предыдущей задачи. Функция должна извлекать ключи словаря для заголовков столбца из
# переданного файла.

import pickle
import csv

__all__ = ["pickle_to_csv"]


def pickle_to_csv():
    with open('user.pickle', 'rb') as pickle_file:
        data = pickle.load(pickle_file)

    fields = ['i', 'a', 'c']

    with open('users.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fields)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv()
