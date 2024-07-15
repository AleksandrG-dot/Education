import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    # id транзакций в USD 939719570, 142264268, 895315941
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268
    assert next(usd_transactions)["id"] == 895315941

    # Ошибка StopIteration
    with pytest.raises(StopIteration):
        assert next(usd_transactions)

    # Отсутствие транзакций в указанной валюте
    usd_transactions = filter_by_currency(transactions, "CNY")
    assert next(usd_transactions) == "Нет транзакций в указанной валюте"

    # Пустой список
    usd_transactions = filter_by_currency([], "CNY")
    assert next(usd_transactions) == "Нет транзакций в указанной валюте"


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert (next(descriptions)) == "Перевод организации"
    assert (next(descriptions)) == "Перевод со счета на счет"
    assert (next(descriptions)) == "Перевод со счета на счет"
    assert (next(descriptions)) == "Перевод с карты на карту"
    assert (next(descriptions)) == "Перевод организации"

    # Пустой список вызывает исключение StopIteration
    descriptions = transaction_descriptions([])
    with pytest.raises(StopIteration):
        assert next(descriptions)

    # Список из двух элементов
    descriptions = transaction_descriptions([{"description": "Перевод в Сбер"}, {"description": "Перевод в ВТБ"}])
    assert (next(descriptions)) == "Перевод в Сбер"
    assert (next(descriptions)) == "Перевод в ВТБ"

    # Ошибка StopIteration
    with pytest.raises(StopIteration):
        assert next(descriptions)


def test_card_number_generator():
    # Проверка генератора номмеров карт на диапазоне номеров от 999 до 1222
    for i, card_number in enumerate(card_number_generator(999, 1222), start=999):
        assert int(card_number.replace(" ", "")) == i

    # Исключение ValueError при значениях больше 16 цифр
    with pytest.raises(ValueError):
        generate_card = card_number_generator(9999999999999999, 10000000000000000)
        assert next(generate_card)


# Крайние положения
@pytest.mark.parametrize("number, result", ((0, "0000 0000 0000 0000"), (9999999999999999, "9999 9999 9999 9999")))
def test_card_number_generator_0_9(number, result):
    generate_card = card_number_generator(number, number)
    assert next(generate_card) == result
