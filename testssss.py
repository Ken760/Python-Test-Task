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

# response = s.get(url, headers=header)
# sleep(1)
auth = s.post(url, data=data, headers=header, allow_redirects=True)
# profile_page = s.get('https://siriust.ru/profiles-update/', headers=header)
favorites = s.get('https://siriust.ru/wishlist/', headers=header)
# print(favorites.text)


favorite_links = []

all_reviews = []
count = 0
lst = []


favorite = BeautifulSoup(favorites.text, "lxml")
for link in favorite.find_all('a', class_='product-title'):
    favorite_links.append(link['href'])

# print(favovite_link)
for links in favorite_links:
    all_favorite_links = s.get(links)

    soup = BeautifulSoup(all_favorite_links.text, 'lxml')
    title = soup.find('h1', class_='ty-product-block-title').text
    retail_price = soup.find_all('span', class_='ty-price-num')[0].text.strip().replace(u'\xa0', u' ')
    wholesale_price = soup.find_all('span', class_='ty-price-num')[2].text.strip().replace(u'\xa0', u' ')
    # shops = soup.find_all('div', class_='ty-product-feature__value')
    # for i in shops:
    #     test = i.text.strip().replace('—  ', '')
    #     if test != 'отсутствует' and test != '':
    #         count += 1
    #
    # reviews_count = soup.find('a', class_='ty-discussion__review-a cm-external-click')

    # all_reviews = []
    # count_reviews = 0
    #
    # reviews = soup.find_all('div', class_='ty-discussion-post__message')
    # for count, review in enumerate(reviews, start=1):
    #     all_reviews.append(review.text)

    lst.append({
        'title': title,
        'розничная цена': retail_price,
        'оптовая цена': wholesale_price,
        # 'количество магазинов, в которых есть товар': count,
        # 'Отзывы': all_reviews
    })
    print(lst)
    # reviews = soup.find_all('div', class_='ty-discussion-post__message')
    # for i, review in reviews:
    #     if review is not None:
    #         all_reviews.append(review.text)
    # print(reviews)


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



# tests = s.get('https://siriust.ru/zapchasti-dlya-apple-i-psp/zapchasti-dlya-apple-iphone/displei-original-dlya-iphone/displey-dlya-iphone-xtachskrin-chernyy-org-ref/', headers=header)
# test = BeautifulSoup(tests.text, "lxml")
#
# price = test.find('h1', class_='ty-product-block-title')
# price(price)