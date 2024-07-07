# Виджет банковских операций

Пакет содержит модули:
- masks - работа с маскировками;
- processing - работа с данными транзакций;
- widget - работа с данными виджета.

## Функции и примеры
### masks

- get_mask_card_number(<card_number>) - возвращает замаскированную строку с номером карты.  
masks.get_mask_card_number(2202178535162089) -> "2202 17** **** 2089"
- get_mask_account(<account_number>) - возвращает замаскированный номер счета  
masks.get_mask_account(73654108430135874305) -> "**4305"

### processing
- filter_by_state(<transaction_list>) - фильтрует список транзакций по ключу state (по умолчанию, EXECUTED)
- sort_by_date(<transaction_list>) - сортирует список транзакций по дате совершения (по умолчанию - убывание)

### widget
- mask_account_card(<card_or_account>) - возвращает маскированный счет или карту  
widget.mask_account_card("Visa Platinum 7000 7922 8960 6361") -> "Visa Platinum  7000 79** **** 6361"  
widget.mask_account_card("Счет 64686473678894779589")    -> "Счет **9589"
- get_date( datе ) - конвертирует время из формата ISO 8601 в ДД.ММ.ГГГГ  
widget.get_date("2024-03-11T02:26:18.671407") -> "11.03.2024"

# Инструкция по установке
Чтобы скачать репозиторий:

`git clone https://github.com/AleksandrG-dot/Education.git`


