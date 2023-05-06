import requests as rqs
from bs4 import BeautifulSoup as BS
import urllib3
from time import sleep

#Авторизация на сайте

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'

header = {
    'user-agent': user_agent
}

data = {
    "return_url": "index.php",
    "redirect_url": "index.php",
    "user_login": "nehnaev@gmail.com",
    "password":	"ThooVur4dave",
    "dispatch[auth.login]": ""
}

url = 'https://siriust.ru'

s = rqs.session()

response = s.get(url, headers=header)
sleep(2)
auth = s.post(url, data=data, headers=header, allow_redirects=True)
test = s.get('https://siriust.ru/profiles-update/', headers=header)
print(test.text)
# print(auth.text)

# link = 'https://siriust.ru/profiles-update/'# Код страницы, который нужно спрасить
#
# r = s.get(link, verify=False).text
# soup = BS(r, 'lxml')
# print(soup.prettify())