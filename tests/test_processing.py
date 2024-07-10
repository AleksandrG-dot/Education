import pytest

from src.processing import filter_by_state, sort_by_date


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
