import requests
from bs4 import BeautifulSoup
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
    soup = BeautifulSoup(profile_page.text, "lxml")
    email = soup.find_all('input', class_="ty-input-text cm-focus")[0]['value']
    first_name = soup.find_all('input', class_="ty-input-text cm-focus")[1]['value']
    last_name = soup.find_all('input', class_="ty-input-text")[12]['value']

    city = soup.find_all('input', class_="ty-input-text")[15]['value']
    profile_info.append((email, first_name, last_name, city))
    return profile_info


def get_favourite_page():
    """Функция получения данных из избранных товаров"""
    get_auth()
    favorites = s.get('https://siriust.ru/wishlist/', headers=header)
    favorite_links = []
    favorite = BeautifulSoup(favorites.text, "lxml")
    for link in favorite.find_all('a', class_='product-title'):
        favorite_links.append(link['href'])

    for links in favorite_links:
        count = 0
        all_reviews = []
        all_ratings = ''
        reviews_text = ''
        all_favorite_links = s.get(links)
        soup = BeautifulSoup(all_favorite_links.text, 'lxml')
        title = soup.find('h1', class_='ty-product-block-title').text
        retail_price = soup.find_all('span', class_='ty-price-num')[0].text.strip().replace(u'\xa0', u' ')
        wholesale_price = soup.find_all('span', class_='ty-price-num')[2].text.strip().replace(u'\xa0', u' ')
        rating = soup.find_all('div', class_='ty-product-block__rating')
        for star in rating:
            ratings = star.find_all('i', class_='ty-stars__icon ty-icon-star')
            all_ratings = len(ratings)
        shops = soup.find_all('div', class_='ty-product-feature__value')
        for shop in shops:
            available = shop.text.strip().replace('—  ', '')
            if available != 'отсутствует' and available != '':
                count += 1

        reviews = soup.find_all('div', class_='ty-discussion-post__message')
        for review in reviews:
            all_reviews.append(review.text)
        for text_reviews in all_reviews:
            reviews_text = all_reviews
        number_of_reviews = soup.find('a', 'ty-discussion__review-a cm-external-click')
        if number_of_reviews is None:
            star_reviews = 0
        else:
            star_reviews = int(number_of_reviews.text[0])
        favourite_list.append(
            (title, retail_price, wholesale_price, all_ratings, count, str(reviews_text), star_reviews))


def add_db():
    """Функция добавления данных в базу"""
    get_profile_page()
    get_favourite_page()
    conn = sqlite3.connect("mydata1.db")
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO siriust VALUES (?, ?, ?, ?)", profile_info)
    cursor.executemany("INSERT INTO favorites VALUES (?, ?, ?, ?, ?, ?, ?)", favourite_list)
    conn.commit()
    conn.close()


add_db()