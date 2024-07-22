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


@pytest.fixture()
def transactions():
    return [
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
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
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
