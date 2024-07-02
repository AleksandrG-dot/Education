from src import masks, widget
# from src import widget

print(masks.get_mask_card_number(2202567890234554))
print(masks.get_mask_account(73654108430135874305))

inp_card_or_account = ['Visa Platinum 7000 7922 8960 6361',
                       'Maestro 1596837868705199',
                       'Счет 64686473678894779589',
                       'MasterCard 7158300734726758',
                       'Счет 35383033474447895560',
                       'Visa Classic 6831982476737658',
                       'Visa Platinum 8990922113665229',
                       'Visa Gold 5999414228426353',
                       'Счет 73654108430135874305']

for i in inp_card_or_account:
    print(widget.mask_account_card(i))