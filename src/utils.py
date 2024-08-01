import json

from src import external_api


def downloading_financial_transaction_data(path: str) -> list[dict]:
    """Функция читает из JSON-файла данные о финансовых транзакция и возвращает список словарей"""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        data = []
    return data


def get_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях. Если исходная транзакция не в рублях, то переводит
    в рубли по текущему курсу. На вход получает тразакцию."""
    result = transaction["operationAmount"]["amount"]
    currency = transaction["operationAmount"]["currency"]["code"]
    if currency != "RUB":
        result = external_api.conversion_in_rub(result, currency)
    return float(result)
