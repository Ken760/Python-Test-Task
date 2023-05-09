import sqlite3

conn = sqlite3.connect("mydata.db")

sql_profile = "CREATE TABLE profile (email TEXT, first_name TEXT, last_name TEXT, city TEXT)"
sql_favorites = "CREATE TABLE favorites (title TEXT, retail_price INT, wholesale_price INT, all_ratings INT, count_shop INT, reviews_text TEXT, star_reviews INT)"

cursor = conn.cursor()

cursor.execute(sql_profile)
cursor.execute(sql_favorites)

res = cursor.fetchall()

conn.close()
