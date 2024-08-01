from unittest.mock import patch

import pytest

from src.utils import downloading_financial_transaction_data, get_amount


# Тестирование функции чтения транзакций из файла
# Тест на чтение реального файла и сверка одного из значений списка
def test_downloading_financial_transaction_data():
    assert downloading_financial_transaction_data(r'data\operations.json')[1] == {'id': 41428829, 'state': 'EXECUTED',
                                                                                  'date': '2019-07-03T18:35:29.512364',
                                                                                  'operationAmount': {
                                                                                      'amount': '8221.37',
                                                                                      'currency': {'name': 'USD',
                                                                                                   'code': 'USD'}},
                                                                                  'description': 'Перевод организации',
                                                                                  'from': 'MasterCard 7158300734726758',
                                                                                  'to': 'Счет 35383033474447895560'}


# Тест на чтение не существующего файла. Должен вернуться пустой список.
def test_downloading_financial_transaction_data_not_file():
    assert downloading_financial_transaction_data('any_file.json') == []


# Тест на чтение существующего файла с неверным форматом JSON. Должен вернуться пустой список.
def test_downloading_financial_transaction_data_no_correct_json():
    assert downloading_financial_transaction_data(r'tests\data\no_correct.json') == []


# Тестирование функции, получающей на вход транзакцию и возвращающей сумму транзакции
# Транзакция в RUB, сторонний API не используется, Возврат типа float.
def test_get_amount_rub():
    transac = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "4567.89",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    assert get_amount(transac) == 4567.89


# У транзакции нет одного из необходимых ключей, сторонний API не используется, Возврат - исключение.
def test_get_amount_rub():
    transac = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "4567.89",
        },
    }
    with pytest.raises(KeyError) as exc_info:
        get_amount(transac)
    assert str(exc_info.value) == "'currency'"

    # Пустая транзакция []
    with pytest.raises(TypeError) as exc_info:
        get_amount([])


# Транзакция в USD, сторонний API используется, Возврат типа float.
# Используется декоратор-заглушка path
@patch('src.external_api.requests.get')
def test_get_amount_usd(moc_get):
    transac = {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {
            "amount": "1000.00",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366"
    }
    moc_get.return_value.status_code = 200
    moc_get.return_value.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 1000},
                                              'info': {'timestamp': 1722533884, 'rate': 85.503972},
                                              'date': '2024-08-01', 'result': 85503.97}
    assert get_amount(transac) == 85503.97
    moc_get.assert_called_once()

# Транзакция неизвестной валюте, сторонний API используется, API код не равен 200
# Возврат - исключение Exception("Unsupported currency")
# Используется декоратор-заглушка path
@patch('src.external_api.requests.get')
def test_get_amount_err(moc_get):
    transac = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {
                "name": "LUNA",
                "code": "LUNA"
            }
        },
    }
    moc_get.return_value.status_code = 400
    moc_get.return_value.json.return_value = {'result': 85503.97}
    with pytest.raises(Exception) as exc_info:
        get_amount(transac)
    assert str(exc_info.value) == "Unsupported currency"

    moc_get.assert_called_once()

