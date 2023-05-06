import requests
from time import sleep

session = requests.Session()


def autorithation():

    session = requests.Session()

    url = 'https://siriust.ru?redirect_url=index.php&user_login=nehnaev@gmail.com&password=ThooVur4dave'

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'

    # header = {
    #     'user-agent': user_agent,
    #     "return_url": "index.php",
    #     "redirect_url": "index.php",
    #     "user_login": "nehnaev@gmail.com",
    #     "password": "ThooVur4dave",
    #     "dispatch[auth.login]": ""
    # }
    #
    # datas = {
    #     "return_url": "index.php",
    #     "redirect_url": "index.php",
    #     "user_login": "nehnaev@gmail.com",
    #     "password":	"ThooVur4dave",
    #     "dispatch[auth.login]": ""
    # }

    responce = session.post(url)
    return responce

def get_history():
    sleep(3)
    auth = autorithation()
    base_url = 'https://siriust.ru/profiles-update/'
    responce = session.get(base_url, cookies=auth.cookies).text
    return responce

print(get_history())