# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


import csv
import json
import os
from pathlib import Path

path_ = input('Введите адрес: ')
adres_dict = {}

def folderSize(path):
    fsize = 0
    numfile = 0
    iteration = 0
    for file in Path(path).rglob('*'):
        if (os.path.isfile(file)):
            fsize += os.path.getsize(file)
            numfile +=1
        iteration+=1
    return fsize

def func(path):
        for root, dirs, files in os.walk(path, topdown = False, onerror = None, followlinks = True):
                id = 0
                for name in dirs:
                        folder_size = folderSize(root)
                        adres_dict.update({id : os.path.join(root,name) + ' -> dir, size = ' + str(folder_size)})
                        id +=1
                for name in files:
                        # size = os.path.getsize(path_)
                        file_path = os.path.join(root, name)
                        size = os.path.getsize(file_path)
                        adres_dict.update({id: os.path.join(root,name) + ' -> file, size = ' + str(size)})
                        id +=1
                

        with open('walk.json', 'w', encoding = 'utf-8') as file:
                json.dump(adres_dict, file)
        
        with open('walk.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=adres_dict)
                writer.writeheader()
                writer.writerow(adres_dict)

func(path_)

