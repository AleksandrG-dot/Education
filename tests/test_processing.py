import pytest

from src.processing import category_counter, filter_by_description, filter_by_state, sort_by_date


# Тестирование функции фильтра транзакций filter_by_state
def test_filter_by_state(transaction_list, transaction_list_executed, transaction_list_canceled):
    # Тестирование фильтрации списка словарей по статусу state = "EXECUTED"
    assert filter_by_state(transaction_list, state="EXECUTED") == transaction_list_executed

    # Тестирование фильтрации списка словарей по статусу state = "CANCELED"
    assert filter_by_state(transaction_list, state="CANCELED") == transaction_list_canceled

    # Тестирование при отсутствии статуса state в словаре
    assert filter_by_state(transaction_list, state="EXPECTS") == []

    # Параметризация тестов для различных возможных значений статуса state


@pytest.mark.parametrize("state_arg", ("", 1, 2.0, True, ()))
def test_filter_by_state_1(transaction_list, state_arg):
    assert filter_by_state(transaction_list, state=state_arg) == []


# Тестирование функции сортировки по дате sort_by_date
def test_sort_by_date(transaction_list, transaction_list_same_dates, transaction_list_non_standart):
    # Тестирование по убыванию
    assert sort_by_date(transaction_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    # Тестирование по возрастанию
    assert sort_by_date(transaction_list, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

    # Тестирование сортировки при одинаковых датах
    assert sort_by_date(transaction_list_same_dates) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-07-10T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-07-10T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-07-10T02:08:58.425572"},
    ]

    # Тестирование сортировки c некорректными или нестандартными форматами дат
    assert sort_by_date(transaction_list_non_standart) == [
        {"id": 126, "state": "CANCELED", "date": "20240710T19441"},
        {"id": 125, "state": "CANCELED", "date": "20230202T5.241689"},
        {"id": 124, "state": "EXECUTED", "date": "20201212T572"},
        {"id": 123, "state": "EXECUTED", "date": "20190703T12364"},
    ]


# Тестирование функции фильтра транзакций по описанию filter_by_description
def test_filter_by_description(transactions):
    # Тестирование фильтрации по строке 'Перевод организации'
    assert filter_by_description(transactions, "Перевод организации") == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    # Тестирование фильтрации по строке 'Перевод с карты на карту'
    assert filter_by_description(transactions, "Перевод с карты на карту") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    ]

    # Тестирование фильтрации со строкой не имеющейся в списке транзакций
    assert filter_by_description(transactions, "any") == []

    # Тестирование фильтрации с пустым списком
    assert filter_by_description([], "any") == []


# Тестирование функции подсчета количества указанных категорий category_counter
def test_category_counter(transactions):
    # Подсчет категорий 'Перевод организации', 'Перевод с карты на карту'
    assert category_counter(transactions, ["Перевод организации", "Перевод с карты на карту"]) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }

    # Подсчет не существующих операций
    assert category_counter(transactions, ["Перевод", "Что-то еще"]) == {}

    # Подсчет в пустом словаре
    assert category_counter([], ["Перевод организации"]) == {}
