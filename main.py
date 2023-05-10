import requests
from lxml import html
import sqlite3

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'

header = {
    'user-agent': user_agent
}

login = input('Введите email: ')
password = input('Введите пароль: ')

data = {
    "return_url": "index.php",
    "redirect_url": "index.php",
    "user_login": login,
    "password": password,
    "dispatch[auth.login]": ""
}

url = 'https://siriust.ru'
s = requests.session()

favourite_list = []
profile_info = []


def get_auth():
    """Функция авторизации"""
    auth = s.post(url, data=data, headers=header, allow_redirects=True)
    return auth


def get_profile_page():
    """Функция получения данных из профиля"""
    get_auth()
    profile_page = s.get('https://siriust.ru/profiles-update/', headers=header)
    profile = html.fromstring(profile_page.text)
    email = profile.xpath('//*[@id="email"]/@value')
    first_name = profile.xpath('//*[@id="elm_15"]/@value')
    last_name = profile.xpath('//*[@id="elm_17"]/@value')
    city = profile.xpath('//*[@id="elm_23"]/@value')
    profile_info.append((*email, *first_name, *last_name, *city))


def get_favourite_page():
    """Функция получения данных из избранных товаров"""
    get_auth()
    favorites = s.get('https://siriust.ru/wishlist/', headers=header)
    favorite_links = []
    favorite = html.fromstring(favorites.text)
    for link in favorite.xpath('//a[@class="product-title"]/@href'):
        favorite_links.append(link)
    for links in favorite_links:
        available_counter = 0
        all_reviews = []
        all_ratings = ''
        all_favorite_links = s.get(links)
        favourite = html.fromstring(all_favorite_links.text, 'lxml')
        title = favourite.xpath('//*[@id="tygh_main_container"]/div[3]/div/div[1]/div/div/div[1]/div/h1/bdi')[0].text.strip()
        retail_price = favourite.cssselect('span.ty-price-num')[0].text.strip().replace(u'\xa0', u' ')
        wholesale_price = favourite.cssselect('span.ty-price-num')[2].text.strip().replace(u'\xa0', u' ')
        rating = favourite.xpath('//*[@id="tygh_main_container"]/div[3]/div/div[1]/div/div/div[1]/div/div[3]/div/div[1]/div[1]')
        for star in rating:
            ratings = star.xpath('//*[@id="average_rating_product"]/span/a/i')
            all_ratings = len(ratings)
        reviews = favourite.cssselect('div.ty-discussion-post__message')
        for review in reviews:
            all_reviews.append(review.text)
        number_of_reviews = favourite.xpath('//*[@id="average_rating_product"]/a[1]')
        if not number_of_reviews:
            star_reviews = 0
        else:
            star_reviews = int(number_of_reviews[0].text[0])
        shops = favourite.xpath('//*[@id="content_features"]/div/div/div/text()')
        for shop in shops:
            available = shop.strip().replace('—  ', '')
            if available != 'отсутствует' and available != '':
                available_counter += 1
        favourite_list.append(
            (title, retail_price, wholesale_price, all_ratings, available_counter, str(all_reviews), star_reviews))


def add_db():
    """Функция добавления данных в базу"""
    get_profile_page()
    get_favourite_page()
    conn = sqlite3.connect("mydata.db")
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO profile VALUES (?, ?, ?, ?)", profile_info)
    cursor.executemany("INSERT INTO favorites VALUES (?, ?, ?, ?, ?, ?, ?)", favourite_list)
    conn.commit()
    conn.close()


add_db()