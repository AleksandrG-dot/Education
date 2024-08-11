import json
import logging

from src import external_api

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def downloading_financial_transaction_data(path: str) -> list[dict]:
    """Функция читает из JSON-файла данные о финансовых транзакция и возвращает список словарей"""
    logger.info(f"Запуск функции чтения JSON-файла downloading_financial_transaction_data({path})")
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        logger.error(f"Функция downloading_financial_transaction_data: Произошла ОШИБКА: {e}", exc_info=True)
        data = []
    logger.info("Завершение работы функции чтения JSON-файла downloading_financial_transaction_data")
    return data


def get_amount(transaction: dict) -> float:
    """Возвращает сумму транзакции в рублях. Если исходная транзакция не в рублях, то переводит
    в рубли по текущему курсу. На вход получает тразакцию."""
    logger.info("Запуск функции возвращающей сумму транзацкии get_amount")
    try:
        result = transaction["operationAmount"]["amount"]
        currency = transaction["operationAmount"]["currency"]["code"]
    except Exception as e:
        logger.error(f"Функция get_amount: Произошла ОШИБКА: {e}", exc_info=True)
        raise e
    if currency != "RUB":
        logger.info("Функция get_amount: Запрос котировок через API")
        try:
            result = external_api.conversion_in_rub(result, currency)
        except Exception as e:
            logger.error(
                f"Ф. get_amount: external_api.conversion_in_rub({result}, {currency}): Произошла ОШИБКА: {e}",
                exc_info=True,
            )
            raise e
    logger.info("Завершение работы функции возвращающей сумму транзацкии get_amount")
    return float(result)
