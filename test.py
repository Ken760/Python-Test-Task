import requests


def main():
    # datas = {
    #     'user_login': '',
    #     'password': ''
    # }
    base_url = 'https://siriust.ru/login'
    # url_login = base_url = '/login'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/75.0.3770.142 Safari/537.36'
    # login = input('Enter email: ')
    # passwd = input('Enter password: ')
    # datas['user_login'] = login
    # datas['password'] = passwd
    s = requests.Session()
    s.headers.update({'User-Agent': user_agent})
    # loging = s.post(url_login, data=datas)
    login = input('Enter email: ')
    passwd = input('Enter password: ')
    resp = s.post(base_url, {
        'user_login': login,
        'password': passwd,
      })

    # запись ответа в файл
    with open('success_login.txt', 'w', encoding='utf-8') as f:
        f.write(resp.text)


if __name__ == "__main__":
    main()

    # f = open('result.txt', 'w', encoding='utf-8')
    # f.write(loging.text)
    # f.close()
    # url_wishlist = 'https://siriust.ru/wishlist/'

    # url = "https://siriust.ru/"
    #
    # payload={'user_login': 'nehnaev@gmail.com',
    # 'password': 'ThooVur4dave'}
    # files=[
    #
    # ]
    # headers = {}
    #
    # response = requests.request("POST", url, headers=headers, data=payload, files=files)
    #
    # print(response.text)

# print(autorithation())