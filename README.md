# Виджет банковских операций

Пакет содержит модули:
- masks - работа с маскировками;
- processing - работа с данными транзакций;
- widget - работа с данными виджета.

## Инструкция по установке
Чтобы скачать репозиторий:  
`git clone https://github.com/AleksandrG-dot/Education.git`


## Зависимости и конфигурация
The program uses the version Python 3.12.4
black==24.4.2
click==8.1.7
colorama==0.4.6
coverage==7.5.4
flake8==7.1.0
iniconfig==2.0.0
isort==5.13.2
mccabe==0.7.0
mypy==1.10.1
mypy-extensions==1.0.0
packaging==24.1
pathspec==0.12.1
platformdirs==4.2.2
pluggy==1.5.0
pycodestyle==2.12.0
pyflakes==3.2.0
pytest==8.2.2
pytest-cov==5.0.0
typing_extensions==4.12.2

*Для установки зависимостей выполните команду:  
`pip install -r requirements.txt`

## Функции и примеры
### Модуль masks

- get_mask_card_number(<card_number>) - возвращает замаскированную строку с номером карты.  
`masks.get_mask_card_number(2202178535162089) -> "2202 17** **** 2089"`
- get_mask_account(<account_number>) - возвращает замаскированный номер счета  
`masks.get_mask_account(73654108430135874305) -> "**4305"`

### Модуль processing
- filter_by_state(<transaction_list>) - фильтрует список транзакций по ключу state (по умолчанию, EXECUTED)
- sort_by_date(<transaction_list>) - сортирует список транзакций по дате совершения (по умолчанию - убывание)

### Модуль widget
- mask_account_card(<card_or_account>) - возвращает маскированный счет или карту  
`widget.mask_account_card("Visa Platinum 7000 7922 8960 6361") -> "Visa Platinum  7000 79** **** 6361"`  
`widget.mask_account_card("Счет 64686473678894779589")    -> "Счет **9589"`
- get_date( datе ) - конвертирует время из формата ISO 8601 в ДД.ММ.ГГГГ  
`widget.get_date("2024-03-11T02:26:18.671407") -> "11.03.2024"`

### Модуль generators
- filter_by_currency(<transaction_list>, <currency>) - функция-генератор, фильтрующая список транзакций по ключу "currency"  

`usd_transactions = generators.filter_by_currency(transactions, "USD")`  
`try:`
`for _ in range(2):`  
`print(next(usd_transactions))`  
`except:`  
`pass`
- transaction_descriptions(<transaction_list>) - функция-генератор, возвращающий описание операции транзакции согласно порядку в списке

`try:`
`descriptions = generators.transaction_descriptions(transactions)`   
`for _ in range(5):`
`print(next(descriptions))`
`except:`
`pass`
- card_number_generator(<start>, <stop>) - функция-генератор, возвращающая диапазон карт между start и stop согласно маске "XXXX XXXX XXXX XXXX"  
 
`for card_number in generators.card_number_generator(8, 10):`  
 `print(card_number)`

### Модуль decorators
- декоратор логов `@log` (в файл или терминал)   

`@log  
def example_function(a, b)  
...`


## Тестирование
Модуль тестирования: pytest==8.2.2  
Количество тестов: 60  
Code coverage: 99%


