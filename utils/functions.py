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
        if len(open_files[i]) > 0 and open_files[i]["state"] == "EXECUTED":
            new_sort.append(open_files[i])
    return new_sort


def sort_files(new_files):
    """
    Сортировка файлов по дате и возвращение последних 5 операций
    """
    sorted_files = sorted(new_files, key=lambda x: x['date'], reverse=True)
    return sorted_files[:5]
