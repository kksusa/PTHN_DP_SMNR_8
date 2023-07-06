# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.

import csv
import pickle

__all__ = ["csv_to_pickle_string"]


def csv_to_pickle_string():
    with open('users.csv', 'r', newline='', encoding='utf-8') as csv_file:
        data = csv.reader(csv_file, delimiter=",")

        count = 0
        list_ = []
        for row in data:
            if count == 0:
                a, b, c = [i for i in row]
            else:
                list_.append({a: row[0], b: row[1], c: row[2]})
            count += 1
        print(list_)
    print(pickle.dumps(list_))


if __name__ == '__main__':
    csv_to_pickle_string()
