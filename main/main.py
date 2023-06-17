import datetime
import json
from operator import itemgetter
import os


path = os.path.join('../operations.json')


def read_(file_path):
    """Читает файл, возвращает список"""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_the_last_5(operations: list):
    """Принимает список операций, возвращает последние 5 выполненных операций"""
    correct_operations = []
    for i in operations:
        if 'date' in i.keys() and i['state'] == 'EXECUTED':
            correct_date = str(i['date']).replace('T', ' ', 1)
            i['date'] = datetime.datetime.strptime(correct_date, '%Y-%m-%d %H:%M:%S.%f')
            if 'from' in i.keys() and i['from'].startswith('Счет'):
                i['from'] = 'Счет **' + i['from'][-4:-1]
            correct_operations.append(i)
    return sorted(correct_operations, key=itemgetter('date'), reverse=True)[0:5]


def pretty_result(operations: list):
    """Принимает список из 5 последних выполненных операций,
    выводит на экран список в формате:

    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>"""
    keys = ['id', 'state', 'date', 'operationAmount', 'description', 'from', 'to']
    for i in operations:
        date = i['date'].strftime("%d.%m.%Y")

        for k in keys:
            if k not in i.keys():
                i[k] = ""
        print(f'{date} {i["description"]}\n'
              f'{i["from"]} -> {i["to"]}\n'
              f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n')


result = get_the_last_5(read_(path))
pretty_result(result)
