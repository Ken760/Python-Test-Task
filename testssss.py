import requests
import urllib3
from time import sleep
from bs4 import BeautifulSoup


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

s = requests.session()

response = s.get(url, headers=header)
sleep(1)
auth = s.post(url, data=data, headers=header, allow_redirects=True)
profile_page = s.get('https://siriust.ru/profiles-update/', headers=header)
favorites = s.get('https://siriust.ru/wishlist/', headers=header)
# soup = BeautifulSoup(profile_page.text, "lxml")
# print(soup)
# for c in soup.find_all('input'):
#     print(c)
    # print(first_name)
# list = []
# email = soup.find_all('input', class_="ty-input-text cm-focus")[0]['value']
# print(email)
# first_name = soup.find_all('input', class_="ty-input-text cm-focus")[1]['value']
# print(first_name)
#
# last_name = soup.find_all('input', class_="ty-input-text")[12]['value']
# print(last_name)
# city = soup.find_all('input', class_="ty-input-text")[15]['value']
# print(city)
# result = list.append([email, first_name, last_name, city])
# print(result)
# first_name = soup.find_all('input')
# print(first_name)

# print(email)

# print(city)


favorite = BeautifulSoup(favorites.text, "lxml")
for i in favorite.find_all('a', class_='product-title'):
    print(i)