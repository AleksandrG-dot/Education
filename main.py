# Задача 3 в модуле 2
from src import processing

transaction_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

for item in processing.filter_by_state(transaction_list):
    print(item)
for item in processing.filter_by_state(transaction_list, state="CANCELED"):
    print(item)
print()
for item in processing.sort_by_date(transaction_list, reverse=False):
    print(item)

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
