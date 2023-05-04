import requests

url = "https://siriust.ru/"

payload={'login_username': 'login',
'login_password': 'password'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)