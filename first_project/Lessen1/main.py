#https://api.giphy.com/v1/gifs/search
# ?
# api_key=iRemQ9jTUPtfYqWhxn43o2XUNsnJxkZh
# &
# q=proggraming
# &
# limit=5
# &
# offset=0
# &
# rating=pg-13
# &
# lang=ru
# &
# bundle=messaging_non_clips
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

url = "https://api.giphy.com/v1/gifs/search"

params = {
    "api_key" : os.getenv("API_KEY"),
    "q" : "proggraming",
    "limit" : 15,
    "offset" : 0,
    "rating" : "pg-13",
    "lang" : "ru",
    "bundle" : "messaging_non_clips"}
headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36", "Accept": "*/*"}
respons = requests.get(url, params=params, headers=headers)
j_data = respons.json()
pprint(j_data.get('data'))


with open('gifs.json', 'w') as f:
    json.dump(j_data, f)

for gif in j_data.get('data'):
    print(gif.get('images').get('original').get('url'))

# pprint(j_data)
# проверка если код 200, то мы дальше, что то делаем с кодом
# if respons.status_code==200:
#     print('Do something')
# else:
#     pass

# print(respons,"\n" )
# print(respons.headers,"\n")
# print(respons.text,"\n")