""" Функции виджета """

from src import masks


def mask_account_card(card_or_account: str) -> str:
    """Функция возвращает маскированный номер карты или счета с произвольным входом сохраняя фифференциацию"""
    if type(card_or_account) is not str:
        return "incorrect data"
    if len(card_or_account) < 21:
        return "incorrect data"
    payment_system = ("visa", "maestro", "mastercard")  # Поддерживаемые платежные системы
    tmp_list: list[str] = card_or_account.split()
    if tmp_list[0].lower() == "счет":
        if len(tmp_list) != 2 or (not tmp_list[1].isdigit()) or len(tmp_list[1]) != 20:
            return "incorrect data"
        return "Счет " + masks.get_mask_account(int(tmp_list[1]))
    elif tmp_list[0].lower() in payment_system:
        tmp_paysistem = f"{tmp_list[0]} {tmp_list[1] + ' ' if tmp_list[1].isalpha() else ''}"
        if len(tmp_list) > 3:  # Если номер карты разбит по 4 цифры
            tmp_card_number = "".join(tmp_list[-4:])
        else:  # Если номер карты передан единым числом
            tmp_card_number = "".join(tmp_list[-1])
        if not tmp_card_number.isdigit():
            return "incorrect data"
        if len(tmp_card_number) != 16:
            return "incorrect data"
        tmp_card_number_int = int(tmp_card_number)
        return f"{tmp_paysistem} {masks.get_mask_card_number(tmp_card_number_int)}"
    else:
        return "incorrect data"


def get_date(inp_date: str) -> str:
    """Конвертор времени из ISO 8601 в ДД.ММ.ГГГГ"""
    if inp_date.find("T") != 10 or inp_date.find("-") != 4 or inp_date.count("-") != 2:
        return "incorrect data"
    tmp_date = inp_date.split("T")[0].split("-")
    return ".".join(tmp_date[::-1])
