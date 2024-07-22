def filter_by_currency(transactions_list, currency):
    """Итератор, фильтрующий транзакции в указанной валюте"""
    filtered_transactions = list(
        filter(
            lambda transaction: transaction.get("operationAmount").get("currency").get("code") == currency,
            transactions_list,
        )
    )
    print(filtered_transactions)
    if not transactions_list or len(filtered_transactions) == 0:
        yield "Нет транзакций в указанной валюте"

    for item in filtered_transactions:
        yield item
    # return iter(filtered_transactions)


def transaction_descriptions(transactions_list):
    """Генератор, возвращающий описание операции транзакции по очереди"""
    for item in (description.get("description") for description in transactions_list):
        yield item


def card_number_generator(start, stop):
    """Генератор номеров карт от start до stop включительно"""
    if type(start) is not int or type(stop) is not int:
        raise TypeError("Type error. Please use int type.")
    if 9999999999999999 < start or 9999999999999999 < stop or start < 0 or stop < 0 or start > stop:
        raise ValueError("Incorrect data")
    card_number = (str(x) for x in range(start, stop + 1))
    card_number = map(lambda x: "0" * (16 - len(x)) + x, card_number)
    card_number = map(lambda x: f"{x[0:4]} {x[4:8]} {x[8:12]} {x[12:16]}", card_number)
    return card_number
