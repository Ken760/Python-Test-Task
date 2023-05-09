import sqlite3

conn = sqlite3.connect("mydata.db")

sql_s = "CREATE TABLE siriust (email TEXT, first_name TEXT, last_name TEXT, city TEXT)"
sql_f = "CREATE TABLE favorites (title TEXT, retail_price INT, wholesale_price INT, all_ratings INT, count_shop INT, reviews_text TEXT, star_reviews INT)"

cursor = conn.cursor()

cursor.execute(sql_s)
cursor.execute(sql_f)

res = cursor.fetchall()

conn.close()
