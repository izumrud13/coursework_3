import json


def open_file(path):
    """
    Открытие файла со всеми операциями
    """
    with open(path, 'r', encoding="utf-8") as file:
        open_files = json.load(file)
    return open_files


def sort_operation(files):
    """

    """
    new_sort = []
    for i in range(len(files)):
        if len(files[i]) > 0 and files[i]["state"] == "EXECUTED":
            new_sort.append(files[i])
    return new_sort


def sort_files(new_files):
    """
    """
    sorted_files = sorted(new_files, key=lambda x: x['date'], reverse=True)
    return sorted_files
