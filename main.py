from src import generators, processing, widget
from src.reading_data import read_financial_transactions_csv, read_financial_transactions_excel
from src.utils import downloading_financial_transaction_data


def data_transformation(transactions: list[dict]) -> list[dict]:
    result = []
    for i in transactions:
        tmp_dict = {
            "id": i.get("id"),
            "state": i.get("state"),
            "date": i.get("date"),
            "operationAmount": {
                "amount": i.get("amount"),
                "currency": {"name": i.get("currency_name"), "code": i.get("currency_code")},
            },
            "description": i.get("description"),
            "from": i.get("from"),
            "to": i.get("to"),
        }
        result.append(tmp_dict)
    return result


def main():
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
    )
    output_text = ""
    while not output_text:
        user_answer = input("> ")
        if user_answer == "1":
            output_text = "JSON-файл"
            data = downloading_financial_transaction_data(r"data\operations.json")
        elif user_answer == "2":
            output_text = "CSV-файл"
            data = read_financial_transactions_csv(r"data\transactions.csv")
            data = data_transformation(data)
        elif user_answer == "3":
            output_text = "XLSX-файл"
            data = read_financial_transactions_excel(r"data\transactions_excel.xlsx")
            data = data_transformation(data)
    print(f"\nДля обработки выбран {output_text}\n")

    # Запрос статуса фильтрации и фльтрация
    while True:
        print(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"""
        )
        user_answer = input("> ").upper()
        if user_answer in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        else:
            print(f'Статус операции "{user_answer}" недоступен.')
    print(f'Операции отфильтрованы по статусу "{user_answer}"\n')
    data = processing.filter_by_state(data, user_answer)

    # Запрос сортировки по дате (по возрастанию (1) / по убыванию (2))
    user_answer = ""
    while user_answer not in ["да", "нет"]:
        user_answer = input("Отсортировать операции по дате? Да/Нет ").lower()
    if user_answer == "да":
        while user_answer not in ["1", "2", "по возрастанию", "по убыванию"]:
            user_answer = input("Отсортировать по возрастанию (1) или по убыванию (2)?  ").lower()
        if user_answer == "1" or user_answer == "по возрастанию":
            data = processing.sort_by_date(data, False)
        else:
            data = processing.sort_by_date(data)

    # Запрос фильтрации по валюте RUB и фильтрация
    user_answer = ""
    while user_answer not in ["да", "нет"]:
        user_answer = input("Выводить только рублевые тразакции? Да/Нет ").lower()
    if user_answer == "да":
        data_rub = []
        for item in generators.filter_by_currency(data, "RUB"):
            data_rub.append(item)
        data = data_rub
        data_rub = []
        if data[0] == "Нет транзакций в указанной валюте":
            data = []

    # Запрос на фильтрацию по слову в описании транзакции и фильтрация
    user_answer = ""
    while user_answer not in ["да", "нет"] and data != []:
        user_answer = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет "
        ).lower()
    if user_answer == "да":
        print("Укажите слово для фильтра по описанию: ")
        user_answer = input("> ")
        data = processing.filter_by_description(data, user_answer)
    if data:
        print(f"\nВсего банковских операций в выборке: {len(data)}\n")
        for transaction in data:
            # time_transaction = datetime.datetime.strptime(transaction.get('date').split('T')[0], '%Y-%m-%d')
            # print(f'{time_transaction.strftime('%d.%m.%Y')} {transaction.get('description')}')
            print(f"{widget.get_date(transaction.get('date'))} {transaction.get('description')}")
            if transaction.get("description") == "Открытие вклада":
                print(widget.mask_account_card(transaction.get("to")))
            else:
                print(
                    widget.mask_account_card(transaction.get("from"))
                    + " -> "
                    + widget.mask_account_card(transaction.get("to"))
                )
            print(
                f"Сумма: {transaction.get('operationAmount').get('amount')} \
{transaction.get('operationAmount').get('currency').get('name')}"
            )
            print()
    else:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
