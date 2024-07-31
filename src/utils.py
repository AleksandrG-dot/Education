import json
import os


def downloading_financial_transaction_data(path: str) -> list[dict]:
    """ Функция читает из JSON-файла данные о финансовых транзакция и возвращает список словарей"""
    try:
        print(os.getcwd())
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        data = []
    return data
