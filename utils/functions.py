def mask_card_number(card_number):
    # Видны первые 6 цифр и последние 4, разбитые по блокам по 4 цифры
    return " ".join([card_number[:4], card_number[4:8], card_number[8:12], card_number[12:]])


def mask_account_number(account_number):
    # Видны только последние 4 цифры номера счета
    return f"**{account_number[-4:]}"