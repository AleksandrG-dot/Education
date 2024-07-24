"""Тестирование декоратора логов"""

import pytest

from src.decorators import log


# Тестовая функция с выводом в терминал
@log()
def decor_terminal(x, y):
    return x / y


# Тестирование без ошибок, вывод в терминал
def test_terminal_output_success(capsys):
    decor_terminal(10, 5)
    captured = capsys.readouterr()
    assert captured.out == "decor_terminal ok\n"


# Тестирование с ошибкой, вывод в терминал
def test_terminal_output_error(capsys):
    with pytest.raises(ZeroDivisionError):
        decor_terminal(10, 0)

    captured = capsys.readouterr()
    assert captured.out == "decor_terminal error: ZeroDivisionError. Inputs: (10, 0), {}\n"


# Тестовая функция с выводом в файл
filelog = "mylog.txt"


@log(filelog)
def decor_file(x, y):
    return x / y


# Тестирование без ошибок, вывод в файл
def test_file_output_success():
    decor_file(10, 5)
    with open(filelog, "r", encoding="utf-8") as file:
        log_content = file.read()
    assert log_content == "decor_file ok"


# Тестирование с ошибкой, вывод в файл
def test_file_output_error():
    with pytest.raises(ZeroDivisionError):
        decor_file(10, 0)
    with open(filelog, "r", encoding="utf-8") as file:
        log_content = file.read()
    assert log_content == "decor_file error: ZeroDivisionError. Inputs: (10, 0), {}"
