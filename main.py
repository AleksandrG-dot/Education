# Задача 1 в модуле 3 (homework 12.1)
from src.utils import downloading_financial_transaction_data, get_amount

print(downloading_financial_transaction_data(r"data\operations.json")[10])
# for item in downloading_financial_transaction_data(r'data\operations.json'):
#     print(item)
print("-" * 30)

transac = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}
# transac = []
print(get_amount(transac))

# ------------------------------------------------------------------------------

# Задача 5 в модуле 2
# from src.decorators import log
#
# @log()
# def tst_func(x, y):
#     return x / y
#
# print(tst_func(10, 5))

#
# # Задача 4 в модуле 2
# from src import generators
# transactions = [
#       {     "id": 939719570,
#           "state": "EXECUTED",
#           "date": "2018-06-30T02:08:58.425572",
#           "operationAmount": {
#               "amount": "9824.07",
#               "currency": {
#                   "name": "USD",
#                   "code": "USD"
#               }
#           },
#           "description": "Перевод организации",
#           "from": "Счет 75106830613657916952",
#           "to": "Счет 11776614605963066702"
#       },
#       {
#         "id": 1,
#         "state": "EXECUTED",
#         "date": "2020-11-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "10000.000",
#             "currency": {
#                 "name": "EUR",
#                 "code": "EUR"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#       },
#       {
#         "id": 2,
#         "state": "EXECUTED",
#         "date": "2024-07-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "10999.99",
#             "currency": {
#                 "name": "RUB",
#                 "code": "RUB"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#       },
#       {
#               "id": 142264268,
#               "state": "EXECUTED",
#               "date": "2019-04-04T23:20:05.206878",
#               "operationAmount": {
#                   "amount": "79114.93",
#                   "currency": {
#                       "name": "USD",
#                       "code": "USD"
#                   }
#               },
#               "description": "Перевод с карты на карту",
#               "from": "Счет 19708645243227258542",
#               "to": "Счет 75651667383060284188"
#        }]
#
# usd_transactions = generators.filter_by_currency(transactions, "USD")
# try:
#     for _ in range(2):
#         print(next(usd_transactions))
# except: pass
#
# try:
#     descriptions = generators.transaction_descriptions(transactions)
#     for _ in range(5):
#         print(next(descriptions))
# except: pass
#
# for card_number in generators.card_number_generator(8, 10):
#     print(card_number)

# # Задача 3 в модуле 2
# from src import processing
#
# transaction_list = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# for item in processing.filter_by_state(transaction_list):
#     print(item)
# for item in processing.filter_by_state(transaction_list, state="CANCELED"):
#     print(item)
# print()
# for item in processing.sort_by_date(transaction_list, reverse=True):
#     print(item)

# Задача 2 в модуле 2
# from src import widget
#
#
# inp_card_or_account = [
#     "Visa Platinum 7000 7922 8960 6361",
#     "Maestro 1596837868705199",
#     "Счет 64686473678894779589",
#     "MasterCard 7158300734726758",
#     "Счет 35383033474447895560",
#     "Visa Classic 6831982476737658",
#     "Visa Platinum 8990922113665229",
#     "Visa Gold 5999414228426353",
#     "Счет 73654108430135874305",
# ]
#
# for i in inp_card_or_account:
#     print(widget.mask_account_card(i))
#
# print(widget.get_date("2024-03-11T02:26:18.671407"))

# Задача 1 в модуле 2
# from src import masks
#
#
# print(masks.get_mask_card_number(2202567890234554))
# print(masks.get_mask_account(73654108430135874305))
