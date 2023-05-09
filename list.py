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
# tests = s.get('https://siriust.ru/zapchasti-dlya-noutbukov/zaryadnye-ustroystva/azu-dlya-noutbuka-acer-19v-1.58a-30w-konnektor-5.5-x-1.7/', headers=header)
tests = s.get('https://siriust.ru/zapchasti-dlya-apple-i-psp/zapchasti-dlya-apple-iphone/displei-original-dlya-iphone/displey-dlya-iphone-11tachskrin-servisnyy-orig-100/', headers=header)

test = BeautifulSoup(tests.text, "lxml")
# print(test.text)

# title = test.find('h1', class_='ty-product-block-title').text.strip()
# print(title)
# price = test.find('span', class_='ty-price-num').text.strip()
# print(price)
# # for i in test.find()

# reviews_count = test.find('a', class_='ty-discussion__review-a cm-external-click')



raiting = test.find_all('span', class_='ty-nowrap ty-stars')
print(raiting)
# for star in raiting:
#     test = star.find('i', class_='ty-stars__icon ty-icon-star')
#     print(test)

# for r in raiting:

# text_reviews = ''
# number_of_reviews = test.find('a', 'ty-discussion__review-a cm-external-click')
# if test is None:
#     number_of_reviews = 'Нет отзывов'
# else:
#     number_of_reviews = test.text
# print(raiting_text)
    # if r.find('i', 'ty-icon-star-empty'):
    #     print(0)





# print(reviews.text)
# star = test.find_all('i', class_='ty-stars__icon ty-icon-star')
# for i in enumerate(star):
#     print(i)
#

# print(star)

# #

# # for review in reviewss:
# #     if review is not None:
# #         reviews.append(review.text)
# # print(reviews)
# #
# all_reviews = []
# count_reviews = 0
#
# reviews = test.find_all('div',  class_='ty-discussion-post__message')
# for count, review in enumerate(reviews, start=1):
#     all_reviews.append(review.text)
#     if count == '':
#         print('нет отзывов')
#
# print(all_reviews)
# print(count)
# print(reviews)
# all_reviews = []
# count_reviews = 0

# print(i + 1)
    # reviews.append(news_item.text)
# print(all_reviews)

# shop = test.find_all('div', 'ty-product-feature')
# print(shop)

# count = 0
# shops = test.find_all('div', class_='ty-product-feature__value')
# for i in shops:
#     test = i.text.strip().replace('—  ', '')
#     if test != 'отсутствует' and test != '':
#         count += 1
# print(count)
    # print(test)
    # print(test)

    # test = i.find('&nbsp')
    # print(test)

