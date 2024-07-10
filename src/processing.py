def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает транзакции в зависимости от статуса, по умолчанию - выполненные транзакции (EXECUTED)"""
    temp_list = list()
    for item in list_dict:
        if item["state"] == state:
            temp_list.append(item)
    return temp_list


def sort_by_date(list_dict: list[dict], reverse: bool = True) -> list[dict]:
    """Функция сортирует транзакции по дате выполнения, по умолчанию - убывание"""
    return sorted(list_dict, key=lambda x: x["date"], reverse=reverse)
