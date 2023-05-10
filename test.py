import requests
from lxml import html
from time import sleep
import sqlite3

from lxml.cssselect import CSSSelector

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'

header = {
    'user-agent': user_agent
}

# login = input('Введите email: ')
# password = input('Введите пароль: ')

data = {
    "return_url": "index.php",
    "redirect_url": "index.php",
    "user_login": 'nehnaev@gmail.com',
    "password": 'ThooVur4dave',
    "dispatch[auth.login]": ""
}

url = 'https://siriust.ru'
s = requests.session()

favourite_list = []
profile_info = []

#
# def get_auth():
#     """Функция авторизации"""
auth = s.post(url, data=data, headers=header, allow_redirects=True)

# profile_page = s.get('https://siriust.ru/profiles-update/', headers=header)
# tree = html.fromstring(profile_page.text)



#
# email = tree.xpath('//*[@id="email"]/@value')
# first_name = tree.xpath('//*[@id="elm_15"]/@value')
# last_name = tree.xpath('//*[@id="elm_17"]/@value')
# city = tree.xpath('//*[@id="elm_23"]/@value')
# print(*email, *first_name, *last_name, *city)
# profile_info.append((*email, *first_name, *last_name, *city))


# favorites = s.get('https://siriust.ru/wishlist/', headers=header)
# favorite_links = []
# favorite = html.fromstring(favorites.text)
# for link in tree.clasname('a', class_='product-title'):
#     favorite_links.append(link['href'])

# for links in favorite_links:
#     count = 0
#     all_reviews = []
#     all_ratings = ''
#     reviews_text = ''
#     all_favorite_links = s.get(links)
# all_ratings = ''

# all_reviews = []
# count = 0
# reviews_text = ''


# favorites = s.get('https://siriust.ru/wishlist/', headers=header)
# favorite_links = []
# favorite = html.fromstring(favorites.text)
# for link in favorite.xpath('//a[@class="product-title"]/@href'):
#     favorite_links.append(link)
# for links in favorite_links:
#     count = 0
#     all_reviews = []
#     all_ratings = ''
#     reviews_text = ''
#     all_favorite_links = s.get(links)
#     favourite = html.fromstring(all_favorite_links.text, 'lxml')
# favourite_page = s.get('https://siriust.ru/zapchasti-dlya-apple-i-psp/zapchasti-dlya-apple-iphone/displei-original-dlya-iphone/displey-dlya-iphone-11tachskrin-servisnyy-orig-100/')
#
# favourite = html.fromstring(favourite_page.text)
#     title = favourite.xpath('//*[@id="tygh_main_container"]/div[3]/div/div[1]/div/div/div[1]/div/h1/bdi')[0].text
#     print(title)
#     retail_price = favourite.cssselect('span.ty-price-num')[0].text
#     wholesale_price = favourite.cssselect('span.ty-price-num')[2].text
#     print(retail_price)
#     print(wholesale_price)
#
# rating = favourite.xpath('//*[@id="tygh_main_container"]/div[3]/div/div[1]/div/div/div[1]/div/div[3]/div/div[1]/div[1]')
# for star in rating:
#     ratings = star.xpath('//*[@id="average_rating_product"]/span/a/i')
#     all_ratings = len(ratings)
#
#
# reviews = favourite.cssselect('div.ty-discussion-post__message')
# for review in reviews:
#     all_reviews.append(review.text)
# print(*all_reviews)
#
# number_of_reviews = favourite.xpath('//*[@id="average_rating_product"]/a[1]')
# if not number_of_reviews:
#     star_reviews = 0
# else:
#     star_reviews = int(number_of_reviews[0].text[0])
#
# print(star_reviews)
# item_td = favourite.cssselect("span.ty-price-num")[0].text
# print(item_td)

count = 0
shops = favourite.xpath('//*[@id="content_features"]/div/div/div/text()')
for shop in shops:
    available = shop.replace('—  ', '')
    if available != 'отсутствует' and available != '':
        count += 1
print(count)


