import requests
import json

url = "http://openlibrary.org/search.json"

subject = "Artificial intelligence"

params = {
    "subject" : subject,
    "limit" : 10
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Успешный запрос API!", response.status_code)
else:
    print("Запрос API отклонён с кодом состояния:", response.status_code)

data = json.loads(response.text)

books = data["docs"]

for book in books:
    print("Title", book["title"])
    print("Author", book["author_name"])
    print("Subject", book["subject"])
    print("\n")