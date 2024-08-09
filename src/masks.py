""" Содержит функции, маскирующие номера карт и счетов. """
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs/masks.log')
file_formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера карты."""
    logger.info('Запуск функции маскировки нормера карты get_mask_card_number')
    if type(card_number) is not int:
        logger.error('В функцию get_mask_card_number передано не число')
        raise TypeError("Type error. Please use int type.")
    if card_number < 1000000000000000 or card_number > 9999999999999999:
        logger.error(f'В функцию get_mask_card_number передано число содержащее не 16 цифр: {card_number}')
        raise TypeError("Invalid number of digits. Must be 16 digits.")
    tmp_str = str(card_number)
    logger.info('Завершение работы функции маскировки номера карты get_mask_card_number')
    return f"{tmp_str[0:4]} {tmp_str[4:6]}** **** {tmp_str[12:]}"


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера счета."""
    logger.info('Запуск функции маскировки нормера счета get_mask_account')
    if type(account_number) is not int:
        logger.error('В функцию get_mask_account передано не число')
        raise TypeError("Type error. Please use int type.")
    if account_number < 10000000000000000000 or account_number > 99999999999999999999:
        logger.error(f'В функцию get_mask_account передано число содержащее не 20 цифр: {account_number}')
        raise TypeError("Invalid number of digits. Must be 20 digits.")
    logger.info('Завершение работы функции маскировки номера счета get_mask_account')
    return f"**{str(account_number)[-4:]}"
