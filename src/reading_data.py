""" ДЗ 13.1: Считывание финансовых операций """

import pandas as pd


def read_financial_transactions_csv(path: str) -> list[dict]:
    fin_data = pd.read_csv(path, delimiter=";")
    return fin_data.to_dict(orient="records")


def read_financial_transactions_excel(path: str) -> list[dict]:
    fin_data = pd.read_excel(path)
    return fin_data.to_dict(orient="records")
