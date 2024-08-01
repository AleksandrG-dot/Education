import os
import requests
from dotenv import load_dotenv
def conversion_in_rub(amount: str, currency: str) -> float:
    """ Функция конвертации иностранной валюты в рубли используя
    сторонний API https://apilayer.com/exchangerates_data-api"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    load_dotenv()
    payload = {
        "amount": amount,
        "from": currency,
        "to": "RUB"
    }
    headers = {
        "apikey": str(os.getenv("APILAYER_KEY"))
    }
    response = requests.get(url, headers=headers, params=payload)

    if response.status_code != 200:
        raise Exception("Unsupported currency")

    # Смотрим что отвечает сервер \ нужно для тестов
    # print("response.status_code: ", response.status_code)
    # print("response.json: ", response.json())

    return response.json()["result"]





# response = requests.get(url, headers=headers, params=payload)
#
# status_code = response.status_code
# result = response.json()
#
# print(status_code)
# print(result)


