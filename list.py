import requests
import urllib3
from time import sleep
from bs4 import BeautifulSoup


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'

header = {
    'user-agent': user_agent
}

s = requests.session()

args = []
tests = s.get('https://siriust.ru/zapchasti-dlya-apple-i-psp/zapchasti-dlya-apple-iphone/displei-original-dlya-iphone/displey-dlya-iphone-11tachskrin-servisnyy-orig-100/', headers=header)
test = BeautifulSoup(tests.text, "lxml")
# print(test.text)

title = test.find('h1', class_='ty-product-block-title').text.strip()
print(title)
price = test.find('span', class_='ty-price-num').text.strip()
print(price)
# for i in test.find()
reviews_count = test.find('a', class_='ty-discussion__review-a cm-external-click')

# print(reviews.text)
# star = test.find_all('i', class_='ty-stars__icon ty-icon-star')
# print(star)
reviews = []

for i in test.find_all('div', class_='ty-discussion-post__message'):
    reviews.append(i.text.strip())
    print(reviews)

# shop = test.find_all('div', 'ty-product-feature')
# print(shop)
