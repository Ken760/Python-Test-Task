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

soup = BeautifulSoup(profile_page.text, "lxml")
# print(soup)
for c in soup.find_all('input'):
    pass
# last_name = soup.find('input', class_="ty-input-text cm-focus")
# first_name = soup.find_all('input')
# print(first_name)

# print(email)

# print(city)