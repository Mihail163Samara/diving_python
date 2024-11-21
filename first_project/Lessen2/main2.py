import requests
from bs4 import BeautifulSoup

# from fake_useragent import UserAgent
# ua = UserAgent()
# print(ua.safari)


# url = "https://www.boxofficemojo.com/intl/?ref_=bo_nb_hm_tab"
url = "https://www.boxofficemojo.com"
#лучше отделять главный домен от ссылки на сам объект для скрапинга
# headers = {"User-Agent": ua.random}

headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36", "Accept": "*/*"}
params = {"ref_": "bo_nb_hm_tab"}

# делает так как будто мы в рамкой одно сессии запросы к сайту. Вместо requests пишем дальше везде session
session = requests.session() 

response = session.get(url+"/intl", params=params, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

rows = soup.find_all('tr')

films=[]

for row in rows[2]:
    film={}

    film['area'] = row.find('a', {'class': 'a-link-normal'}).getText()
    print(row)

# проверка:
# test_link = soup.find_all('a', {'class': 'a-link-normal'})
# print(test_link)
# print(response.status_code)



