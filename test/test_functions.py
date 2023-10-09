from utils.functions import mask_card_number, mask_account_number, change_date, sort_files, form_list, open_file

TRANSACTIONS = [
{
    "id": 484201274,
    "state": "EXECUTED",
    "date": "2019-04-11T23:10:21.514616",
    "operationAmount": {
      "amount": "62621.51",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 8193813157568899",
    "to": "МИР 9425591958944146"
  },
  {
    "id": 547682597,
    "state": "EXECUTE",
    "date": "2018-12-29T21:45:18.495053",
    "operationAmount": {
      "amount": "66263.93",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 77977573135347241529",
    "to": "Счет 33062909508148771891"
  },
    # Другие операции...
]


def test_open_file():
    result = open_file('D:/Pyyhon/coursework/utils/operations.json')
    assert result[0]["date"] == "2019-08-26T10:50:58.294041"
    assert len(result[0]) > 0



def test_sort_files():
   assert sort_files(TRANSACTIONS) == [{'date': '2019-04-11T23:10:21.514616',
  'description': 'Перевод с карты на карту',
  'from': 'МИР 8193813157568899',
  'id': 484201274,
  'operationAmount': {'amount': '62621.51',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTED',
  'to': 'МИР 9425591958944146'},
 {'date': '2018-12-29T21:45:18.495053',
  'description': 'Перевод организации',
  'from': 'Счет 77977573135347241529',
  'id': 547682597,
  'operationAmount': {'amount': '66263.93',
                      'currency': {'code': 'RUB', 'name': 'руб.'}},
  'state': 'EXECUTE',
  'to': 'Счет 33062909508148771891'}]



def test_form_list():
    assert form_list(TRANSACTIONS) is None


def test_mask_card_number():
    assert mask_card_number('Sber 8193813157568899') == 'Sber 8193 81** **** 8899'
    assert mask_card_number('Мир 1111111111111111') == 'Мир 1111 11** **** 1111'


def test_mask_account_number():
    assert mask_account_number('11111111') == '**1111'
    assert mask_account_number('1111111122222') == '**2222'


def test_change_date():
    assert change_date("2019-04-11T23:19:21.514616") == "11.04.2019"
    assert change_date("2020-01-21T23:11:21.514611") == "21.01.2020"
    assert change_date("2017-01-01T23:10:22.112612") == "01.01.2017"
