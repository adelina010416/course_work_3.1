import datetime
import json
from operator import itemgetter
import os


path = os.path.join('./operations.json')


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
            if 'from' in i.keys():
                if i['from'].startswith('Счет'):
                    i['from'] = 'Счет **' + i['from'][-4:]
                else:
                    card = i['from'].split(' ')
                    card_num = card[-1]
                    del card[-1]
                    i['from'] = f'{" ".join(card)} {card_num[-16:-12]} {card_num[-12:-10]}** **** {card_num[-4:]}'
            if 'to' in i.keys():
                if i['to'].startswith('Счет'):
                    i['to'] = 'Счет **' + i['to'][-4:]
                else:
                    card = i['to'].split(' ')
                    card_num = card[-1]
                    del card[-1]
                    i['to'] = f'{" ".join(card)} {card_num[-16:-12]} {card_num[-12:-10]}** **** {card_num[-4:]}'

            correct_operations.append(i)
    return sorted(correct_operations, key=itemgetter('date'), reverse=True)[0:5]


def pretty_result(operations: list):
    """Принимает список из 5 последних выполненных операций,
    выводит на экран список в формате:

    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>"""
    keys = ['id', 'state', 'date', 'operationAmount', 'description', 'from', 'to']
    result = []
    for i in operations:
        date = i['date'].strftime("%d.%m.%Y")

        for k in keys:
            if k not in i.keys():
                i[k] = ""
        operation = f'{date} {i["description"]}\n{i["from"]} -> {i["to"]}\n' \
                    f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n'
        result.append(operation)
    return result


# last_operations = get_the_last_5(read_(path))
# [print(i) for i in pretty_result(last_operations)]
