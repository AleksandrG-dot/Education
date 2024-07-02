""" Содержит фунеции, маскирующие номера карт и счетов. """


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера карты."""
    if type(card_number) is not int:
        raise TypeError("Type error. Please use int type.")
    if card_number < 1000000000000000 or card_number > 9999999999999999:
        raise TypeError("Invalid number of digits. Must be 16 digits.")
    tmp_str = str(card_number)
    return f"{tmp_str[0:4]} {tmp_str[4:6]}** **** {tmp_str[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера счета."""
    if type(account_number) is not int:
        raise TypeError("Type error. Please use int type.")
    if account_number < 10000000000000000000 or account_number > 99999999999999999999:
        raise TypeError("Invalid number of digits. Must be 20 digits.")
    return f"**{str(account_number)[-4:]}"
