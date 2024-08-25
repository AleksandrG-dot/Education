from unittest.mock import patch

import pandas as pd
import pytest

from src.reading_data import read_financial_transactions_csv, read_financial_transactions_excel


# Тестирование функции чтения транзакций из файла csv
# Тест на чтение реального файла и сверка одного из значений списка
def test_read_financial_transactions_csv():
    assert read_financial_transactions_csv(r"data\transactions.csv")[0] == {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


# Тестирование функции чтения транзакций из файла csv
# с использованием patch и Mock
@patch("src.reading_data.pd.read_csv")
def test_read_financial_transactions_csv_patch(moc_get):
    test_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2024-02-15T17:30:30Z",
            "amount": 1000.0,
            "currency_name": "Yuan",
            "currency_code": "CNY",
            "from": "Счет 12345678912345678912",
            "to": "Счет 9876543112345678912",
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2024-03-25T19:25:20Z",
            "amount": 2000.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 55555666666777777722",
            "to": "Счет 33344440555556666661",
            "description": "Перевод организации",
        },
    ]
    moc_get.return_value = pd.DataFrame(test_data)
    assert read_financial_transactions_csv("any_file.csv") == test_data
    moc_get.assert_called_once()


# Тестирование функции чтения транзакций из файла csv
# Файл отсутствует
def test_read_financial_transactions_csv_no_file():
    with pytest.raises(FileNotFoundError):
        read_financial_transactions_csv("any_file.csv")


# Тестирование функции чтения транзакций из файла excel
# Тест на чтение реального файла и сверка одного из значений списка
def test_read_financial_transactions_excel():
    assert read_financial_transactions_excel(r"data\transactions_excel.xlsx")[0] == {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


# Тестирование функции чтения транзакций из файла excel
# с использованием patch и Mock
@patch("src.reading_data.pd.read_excel")
def test_read_financial_transactions_excel_patch(moc_get):
    test_data = [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2024-02-15T17:30:30Z",
            "amount": 1000.0,
            "currency_name": "Yuan",
            "currency_code": "CNY",
            "from": "Счет 12345678912345678912",
            "to": "Счет 9876543112345678912",
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2024-03-25T19:25:20Z",
            "amount": 2000.0,
            "currency_name": "Ruble",
            "currency_code": "RUB",
            "from": "Счет 55555666666777777722",
            "to": "Счет 33344440555556666661",
            "description": "Перевод организации",
        },
    ]
    moc_get.return_value = pd.DataFrame(test_data)
    assert read_financial_transactions_excel("any_file.xlsx") == test_data
    moc_get.assert_called_once()


# Тестирование функции чтения транзакций из файла excel
# Файл отсутствует
def test_read_financial_transactions_excel_no_file():
    with pytest.raises(FileNotFoundError):
        read_financial_transactions_excel("any_file.xlsx")
