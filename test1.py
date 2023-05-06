import requests
from bs4 import BeautifulSoup


url = 'https://siriust.ru/login/'

session = requests.session()
session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'

rs = session.get(url)
root = BeautifulSoup(rs.content, 'html.parser')

name_by_value = dict()
for input_el in root.select('#vega_auth_login input[name]'):
    name = input_el['name']
    name_by_value[name] = input_el.get('value', '')

name_by_value['login'] = '1111'
name_by_value['password'] = '2222'

auth_data = {
    f'vega_auth_login[{name}]': value
    for name, value in name_by_value.items()
}

session.headers.update({
    'X-CSRF-Token': name_by_value['_csrf'],
    'X-Requested-With': 'XMLHttpRequest',
})

rs = session.post(url, files=auth_data)
print(rs)