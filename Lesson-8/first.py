# Напишите функцию, которая возвращает размер HTML документа по адресу https://google.com.
# Т.е. нужно получить страницу и вернуть ее размер (количество символов).
import requests


def get_html_size(url):
    headers = {'content-type': 'html'}
    return len(requests.get(url, headers=headers).text)


url = 'https://google.com'
print(get_html_size(url))