from utils.functions import mask_card_number
from utils.functions import mask_account_number


def last_transactions(operations):
    # Отсортируем операции по дате в обратном порядке
    sorted_transactions = sorted(operations, key=lambda t: t["date"], reverse=True)

    # Выводим на экран последние 5 операций
    for i in range(min(5, len(sorted_transactions))):
        transaction = sorted_transactions[i]

        # Форматируем дату перевода
        date = transaction["date"].strftime("%d.%m.%Y")

        # Маскируем номер карты
        masked_card_number = mask_card_number(transaction["card_number"])

        # Маскируем номер счета
        masked_account_number = mask_account_number(transaction["account_number"])

        # Выводим информацию о переводе
        print(f"{date} {transaction['description']}")
        print(f"{masked_card_number} -> {masked_account_number}")
        print(f"{transaction['amount']} {transaction['currency']}")

        # Разделяем операции пустой строкой
        print()
