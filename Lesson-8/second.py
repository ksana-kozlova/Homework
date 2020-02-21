# Напишите функцию, которая принимает три аргумента
# 1)число, количество денег в исходной валюте, float;
# 2)исходная валюта, трехсимвольная строка, str;
# 3)целевая валюта, трехсимвольная строка, str;
# и возвращает количество денег в целевой валюте (тип float).
# Для получения курса валют воспользуйтесь https://api.exchangerate-api.com .

import requests


def exchange_rate(money: float, source_currency: str, target_currency: str):
    url = 'https://api.exchangerate-api.com/v4/latest/' + source_currency
    coefficient = requests.get(url).json()['rates'][target_currency]
    return money * coefficient


print(exchange_rate(100, "USD", "AUD"))
