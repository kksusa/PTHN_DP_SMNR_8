# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import json
import pickle
import os

__all__ = ["json_to_pickle"]


def json_to_pickle(dir_):
    json_files = [i for i in os.listdir(dir_) if i.endswith('.json')]
    for json_file in json_files:
        with (open(os.path.join(dir_, json_file), 'r', encoding='utf-8') as f,
              open(os.path.join(dir_, json_file.rstrip('.json') + '.pickle'), 'wb') as f_p):
            pickle.dump(json.load(f), f_p)


if __name__ == '__main__':
    json_to_pickle(os.getcwd())
    with open('user.pickle', 'rb') as f_pi:
        print(pickle.load(f_pi))
