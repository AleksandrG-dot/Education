import pytest


@pytest.fixture
def no_format():
    return "any string"


# Список транзакций
@pytest.fixture
def transaction_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Список танзакций со "state" = "EXECUTED"
@pytest.fixture
def transaction_list_executed():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


# Список танзакций со "state" = "CANCELED"
@pytest.fixture
def transaction_list_canceled():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Список транзакций с совпадающими датами
@pytest.fixture
def transaction_list_same_dates():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-07-10T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-07-10T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-07-10T08:21:33.419441"},
    ]


# Список транзакций с некорректными или нестандартными датами
@pytest.fixture
def transaction_list_non_standart():
    return [
        {"id": 123, "state": "EXECUTED", "date": "20190703T12364"},
        {"id": 124, "state": "EXECUTED", "date": "20201212T572"},
        {"id": 125, "state": "CANCELED", "date": "20230202T5.241689"},
        {"id": 126, "state": "CANCELED", "date": "20240710T19441"},
    ]


# Список карт и счетов
@pytest.fixture
def card_and_accout():
    return [
        "Visa Platinum 7000 7922 8960 6361",
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]


# Список карт и счетов
@pytest.fixture
def card_and_accout_mask():
    return [
        "Visa Platinum  7000 79** **** 6361",
        "Maestro  1596 83** **** 5199",
        "Счет **9589",
        "MasterCard  7158 30** **** 6758",
        "Счет **5560",
        "Visa Classic  6831 98** **** 7658",
        "Visa Platinum  8990 92** **** 5229",
        "Visa Gold  5999 41** **** 6353",
        "Счет **4305",
    ]
