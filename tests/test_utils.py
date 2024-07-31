from src.utils import downloading_financial_transaction_data


def test_downloading_financial_transaction_data():
    assert downloading_financial_transaction_data(r'data\operations.json')[1] == {'id': 41428829, 'state': 'EXECUTED',
                                                                                  'date': '2019-07-03T18:35:29.512364',
                                                                                  'operationAmount': {
                                                                                      'amount': '8221.37',
                                                                                      'currency': {'name': 'USD',
                                                                                                   'code': 'USD'}},
                                                                                  'description': 'Перевод организации',
                                                                                  'from': 'MasterCard 7158300734726758',
                                                                                  'to': 'Счет 35383033474447895560'}

def test_downloading_financial_transaction_data_not_file():
    assert downloading_financial_transaction_data('any_file') == []

def test_downloading_financial_transaction_data_no_correct_json():
    assert downloading_financial_transaction_data(r'tests\data\no_correct.json') == []


