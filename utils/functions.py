import json

operation = "operations.json"
with open(operation, 'r', encoding='utf-8') as file:
    data_load = json.load(file)

def last_transactions(operation):


    # Отсортируем операции по дате в обратном порядке
    sorted_transactions = sorted(data_load, key=lambda t: t["date"], reverse=True)

    # Выводим на экран последние 5 операций
    for i in range(min(5, len(sorted_transactions))):
        transaction = sorted_transactions[i]

        # Форматируем дату перевода
        date = data_load["date"].strftime("%d.%m.%Y")

        # Маскируем номер карты
        masked_card_number = mask_card_number(transaction["card_number"])

        # Маскируем номер счета
        masked_account_number = mask_account_number(transaction["account_number"])

        # Выводим информацию о переводе
        print(f"{date} {data_load['description']}")
        print(f"{masked_card_number} -> {masked_account_number}")
        print(f"{data_load['amount']} {data_load['currency']}")

        # Разделяем операции пустой строкой
        print()


def bank_cart(data_load):
    return data_load(["from"]).isalpha


def mask_card_number(data_load):
    number = data_load(["from"]).isdigit
    # Видны первые 6 цифр и последние 4, разбитые по блокам по 4 цифры
    return " ".join([number[:4], number[4:8], number[8:12], number[12:]])


def mask_account_number(data_load):
    # Видны только последние 4 цифры номера счета
    return f"**{data_load[id][-4:]}"