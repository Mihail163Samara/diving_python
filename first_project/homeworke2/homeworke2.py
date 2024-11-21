"""Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах
на сайте во всех категориях: название, цену, количество товара в наличии
(In stock (19 available)) в формате integer, описание.
Затем сохранить эту информацию в JSON-файле."""

import re
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

url = "http://books.toscrape.com/"
url_catalog = url + "catalogue/"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) "
                  "AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "CriOS/122.0.6261.62 Mobile/15E148 Safari/604.1"
}
number_page = 1
session = requests.session()
all_books = []

while True:
    page = f'page-{number_page}.html'
    response = session.get(url_catalog + page, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all('li', {'class': 'col-lg-3'})
    if not books:
        break

    for book in books:
        book_info = {}
        name_info = book.find('h3').find('a')
        book_info["name"] = name_info.get('title')
        book_info["url"] = url_catalog + name_info.get("href")

        price_info = book.find('div', {'class': 'product_price'}).find('p', {'class': 'price_color'}).getText()
        try:
            price = re.search(r"[-+]?\d*\.\d+|\d+", price_info).group()
        except:
            price = None
        book_info["price"] = price

        response_in = session.get(book_info["url"], headers=headers)
        soup_in = BeautifulSoup(response_in.text, "html.parser")
        books_des = soup_in.find_all('article', {'class': 'product_page'})
        for book_des in books_des:
            try:
                description = book_des.find_all('p')[3].getText()
            except:
                description = None
            in_stock_info = book_des.find_all('p')[1].getText()
            parts = in_stock_info.split('(')
            if len(parts) > 1:
                part = parts[1].split(')')[0]
                try:
                    in_stock = int(re.search(r"[-+]?\d*\.\d+|\d+", part).group())
                except:
                    in_stock = None

        book_info["in_stock"] = in_stock
        book_info["description"] = description

        all_books.append(book_info)

    print(f'Обработана {number_page} страница.')
    number_page += 1

with open('books.json', 'w') as f:
    json.dump(all_books, f)

pprint(len(all_books))