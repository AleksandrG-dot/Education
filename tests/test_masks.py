import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование маскировки карт get_mask_card_number
@pytest.mark.parametrize(
    "card, expected",
    [
        (5505745328745574, "5505 74** **** 5574"),
        (2202745328743515, "2202 74** **** 3515"),
        (1234567891234567, "1234 56** **** 4567"),
    ],
)
def test_get_mask_card_number_standart(card, expected):
    assert get_mask_card_number(card) == expected


def test_get_mask_card_number_not_int(no_format):
    with pytest.raises(TypeError):
        get_mask_card_number(no_format)


def test_get_mask_card_number_not_format_small():
    with pytest.raises(TypeError):
        get_mask_card_number(550574532874)


def test_get_mask_card_number_not_format_long():
    with pytest.raises(TypeError):
        get_mask_card_number(5505745328747456936)


def test_get_mask_card_number_empty():
    with pytest.raises(TypeError):
        get_mask_card_number()


# Тестирование маскировки счетов get_mask_account
@pytest.mark.parametrize(
    "card, expected",
    [(87925505745328745574, "**5574"), (99722202745328743515, "**3515"), (32211234567891234567, "**4567")],
)
def test_get_mask_account(card, expected):
    assert get_mask_account(card) == expected


def test_get_mask_account_not_int(no_format):
    with pytest.raises(TypeError):
        get_mask_account(no_format)


def test_get_mask_account_not_format_small():
    with pytest.raises(TypeError):
        get_mask_account(550574532874)


def test_get_mask_account_not_format_long():
    with pytest.raises(TypeError):
        get_mask_account(5505745328747456936125465489)


def test_get_mask_account_empty():
    with pytest.raises(TypeError):
        get_mask_account()
