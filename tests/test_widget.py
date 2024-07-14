import pytest

from src.widget import get_date, mask_account_card


# Тест mask_account_card на общий список карт и счетов
def test_mask_account_card(card_and_accout, card_and_accout_mask):
    for i in range(len(card_and_accout)):
        assert mask_account_card(card_and_accout[i]) == card_and_accout_mask[i]


# Тест mask_account_card на различные карты и счета парметризованный
@pytest.mark.parametrize(
    "card_acc, valid",
    [
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa 4111 1111 1111 1111", "Visa  4111 11** **** 1111"),
        ("Visa 4111111111111111", "Visa  4111 11** **** 1111"),
        ("Visa Platinum 4111111111111111", "Visa Platinum  4111 11** **** 1111"),
    ],
)
def test_mask_account_card_2(card_acc, valid):
    assert mask_account_card(card_acc) == valid


# Тест mask_account_card на не корректные данные типа данных (счета или карты) или недостаточность данных
@pytest.mark.parametrize(
    "card_acc",
    [
        "",
        "Счет 12345678901234567890123456",
        "Счот 12345678901234567890",
        "Счод 1236901234567890",
        "Счет **3456",
        "Счет",
        "Счет ",
        "Счет 12@4567890ABC4567890",
        "Viza 4111 1111 1111 1111",
        "Mir 2222211111111111",
        "Visa 2222 3333 4444",
        "Visa 4111 **** **11 1111",
        "Visa 4111 11 1111 1111",
        12,
        (),
        True,
    ],
)
def test_mask_account_card_incorrect_1(card_acc):
    assert mask_account_card(card_acc) == "incorrect data"


# Тестирование функции get_date - Конвертора времени из ISO 8601 в ДД.ММ.ГГГГ
@pytest.mark.parametrize(
    "date, valid",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),  # Корректная дата
        ("2020-03-12T00:00:00.00", "12.03.2020"),  # Корректная дата
        ("2020-T03-120", "incorrect data"),  # Не корректные даты
        ("20-2003-12T", "incorrect data"),
        ("20248-03-11T02:26:18.671407", "incorrect data"),
        ("2024-80-311T02:26:18.671407", "incorrect data"),
        ("202480311T02:26:18.671407", "incorrect data"),  # Нестандартная строка с датой
        ("T02:26:18.671407", "incorrect data"),  # Отсутствует дата
        ("", "incorrect data"),  # Пустая строка
    ],
)
def test_get_date(date, valid):
    assert get_date(date) == valid
