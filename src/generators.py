def filter_by_currency(transactions_list: list[dict], currency: str) -> list[dict]:
    """Итератор, фильтрующий транзакции в указанной валюте"""
    filtered_transactions = list(filter(
        lambda transaction: transaction.get("operationAmount").get("currency").get("code") == currency,
        transactions_list,
    ))
    if not transactions_list or len(list(filtered_transactions)) == 0:
        yield "Нет транзакций в указанной валюте"
    for item in filtered_transactions:
        yield item