import json


def open_file(path):
    """
    Открытие файла со всеми операциями,
    Создание корректного списка из выполненных операций и без пустых операций
    """
    with open(path, 'r', encoding="utf-8") as file:
        open_files = json.load(file)

    new_sort = []
    for i in range(len(open_files)):
        if len(open_files[i]) > 0 and open_files[i]["state"] == "EXECUTED" and 'Перевод' in open_files[i]['description']:
            new_sort.append(open_files[i])
    return new_sort


def sort_files(new_files):
    """
    Сортировка файлов по дате и возвращение последних 5 операций
    """
    sorted_files = sorted(new_files, key=lambda x: x['date'], reverse=True)

    return sorted_files[:5]


def form_list(sort_file):
    for i in sort_file:
        # Изменяем формат даты
        date = change_date(i["date"])

        # Маскируем номер карты отправителя
        masked_card_number = mask_card_number(i["from"])

        # Маскируем номер  карты получателя
        masked_account_number = mask_account_number(i["to"])

        # Выводим информацию о переводе
        print(f"{date} {i['description']}")
        print(f"{masked_card_number} -> Счет {masked_account_number}")
        print(f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}")

        # Разделяем операции пустой строкой
        print()


def mask_card_number(card_number):
    # Видны первые 6 цифр и последние 4, разбитые по блокам по 4 цифры
    name_card = (''.join([x for x in card_number if x.isalpha()]))
    number_card = (''.join([x for x in card_number if x.isdigit()]))
    return f"{name_card} {number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"


def mask_account_number(card_number):
    # Видны только последние 4 цифры номера счета
    return f"**{card_number[-4:]}"


def change_date(date):
    return f'{date[8:10]}.{date[5:7]}.{date[:4]}'
