# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import csv
import json
import os
import sys    

def get_ids(filename) -> set:
    file = open(filename, 'r', encoding = 'utf-8')
    all_ids = set()
    try:
        # data = json.load(file)
        data = csv.DictReader(file, delimiter=';')
        for level in data:
            for uid in level:
                all_ids.add(uid)
    except:
        pass
    file.close()
    return all_ids

def get_data(all_ids: set, filename):
    working_dict: dict[int: dict[int: str]] = {}
    while True:
        name = input("Введите имя: ")
        if name == '':
            break
        user_id = -1
        while user_id < 0 or user_id in all_ids:
            user_id = int(input('Введите идентификатор:'))
        all_ids.add(user_id)
        access_level = 0
        while not 1 <= access_level <=7:
            access_level = int(input('Введите уровень доступа (1 - 7): '))
        if working_dict.get(access_level):
            working_dict.get(access_level).update({user_id: name})
        else:
            working_dict[access_level] = {user_id: name}
        # dump_json(working_dict, filename) #запись в json
        dump_csv(working_dict, filename)
        
def dump_json(wd, filename):
    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(wd, file)
        
def dump_csv(wd, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=wd)
        writer.writeheader()
        writer.writerow(wd)
        
def func():
    # all_ids = get_ids('data2.json')
    # get_data(all_ids, 'data2.json')
    all_ids = get_ids('data.csv')
    get_data(all_ids, 'data.csv')
    
# func()

# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

with open('data.csv', 'r') as csvfile:
    filereader = csvfile.readlines()
    keys_f = filereader[0].rstrip('\n').split(',')
    val_f = filereader[1].rstrip('\n').split(',')
need_d = dict(zip(keys_f, val_f))
names = []
for value in need_d.values():
    key = value[1] + '000000'
    value_n = value[5:-2]
    value_n = value_n.lower()
    names.append({key:value_n})
need_dict = dict(zip(keys_f, names))
print(need_dict)

with open('data3.json', 'w', encoding = 'utf-8') as file:
    json.dump(need_dict, file)