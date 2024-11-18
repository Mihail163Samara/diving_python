import os
import requests
import json
from io import StringIO
from dotenv import load_dotenv
from pprint import pprint
#В целях безопасности апи ключа он не будет пушится на GitHub
# dotenv_path = '.env'
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#Проверяем есть ли в нашем файл с переменным окружением
if os.path.exists(dotenv_path):
# если есть мы загружаем наш путь
    load_dotenv(dotenv_path)

url = "https://api.foursquare.com/v3/places/search"

# Определение параметров для запроса API
city = input("Введите название города: ")
category = input("Введите наименование категории: ")

params = {
    "query": category,
    "near" : city,
    "limit" : 5
}

headers = {
    "Accept": "application/json",
    "Authorization": os.getenv("API_KEY_FOURSQUARED")
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
# Проверка успешности запроса API
if response.status_code == 200:
    print("Успешный запрос. Вот что нашлось по вашему запосу:")
    data = json.loads(response.text)
    venues = data["results"]
    for venue in venues:
        print("Название:", venue["name"])
        print("Адрес:", venue["location"]["formatted_address"])
        print("\n")
else:
    print("Запрос неудадся с кодом состояния:", response.status_code)
    

with open('Search Values.json', 'w') as f:
    json.dump(data, f)
# --------------------------------------------------------------------------------------------------------------------






# # Вывод результатов
# for place in data["results"]:
#     print(f"Название: {place['name']}, Адрес: {place.get('location', {}).get('formatted_address', 'N/A').get('')}")
# # pprint(response.text)


# with open('response_data.json', 'w') as f:
#     json.dump(data, f)