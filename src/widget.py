""" Функции виджета """

from src import masks


def mask_account_card(card_or_account: str) -> str:
    """Функция возвращает маскированный номер карты или счета с произвольным входом сохраняя фифференциацию"""
    payment_system = ("visa", "maestro", "mastercard")  # Поддерживаемые платежные системы
    tmp_list: list[str] = card_or_account.split()
    if tmp_list[0].lower() == "счет":
        return "Счет " + masks.get_mask_account(int(tmp_list[1]))
    elif tmp_list[0].lower() in payment_system:
        tmp_paysistem = f"{tmp_list[0]} {tmp_list[1] + ' ' if tmp_list[1].isalpha() else ''}"
        if len(tmp_list) > 3:  # Если номер карты разбит по 4 цифры
            tmp_card_number = int("".join(tmp_list[-4:]))
        else:  # Если номер карты передан единым числом
            tmp_card_number = int("".join(tmp_list[-1]))
        return f"{tmp_paysistem} {masks.get_mask_card_number(tmp_card_number)}"
    else:
        return "incorrect data"


def get_date(inp_date: str) -> str:
    """Конвертор времени из ISO 8601 в ДД.ММ.ГГГГ"""
    tmp_date = inp_date.split("T")[0].split("-")
    return ".".join(tmp_date[::-1])
