import requests
from time import sleep

def autorithation():
    session = requests.Session()

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'

    header = {
        'user-agent': user_agent
    }
    # login = input('Enter email: ')
    # passwd = input('Enter password: ')
    payload = {
        'user_login': 'nehnaev@gmail.com',
        'password': 'ThooVur4dave'
    }

    url = 'https://siriust.ru'

    # datas['user_login'] = login
    # datas['password'] = passwd
    response = session.post(url, params=payload, headers=header)
    sleep(20)
    f = open('result.html', 'w', encoding='utf-8')
    f.write(response.text)
    f.close()
    # profile_info = "https://siriust.ru/profiles-update/"
    # profile_responce = session.get(profile_info, headers=header)
    # f = open('result.text', 'w+', encoding='utf-8')
    # f.write(profile_responce.text)
    # f.close()


if __name__ == "__main__":
    autorithation()