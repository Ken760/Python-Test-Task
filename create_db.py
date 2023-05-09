# import sqlite3
#
# conn = sqlite3.connect("mydata.db")
#
# sql = "CREATE TABLE siriust (email TEXT, first_name TEXT, last_name TEXT, city TEXT)"
# # sql = "SELECT * FROM siriust"
#
# cursor = conn.cursor()
#
# cursor.execute(sql)
#
# res = cursor.fetchall()
# #
# # for r in res:
# #     print(r)
#
# conn.close()
import sqlite3

conn = sqlite3.connect("mydata1.db")

sql_s = "CREATE TABLE siriust (email TEXT, first_name TEXT, last_name TEXT, city TEXT)"
sql_f = "CREATE TABLE favorites (title TEXT, retail_price INT, wholesale_price INT, all_ratings INT, count_shop INT, text TEXT, star_reviews INT)"
# sql = "SELECT * FROM siriust"

cursor = conn.cursor()

cursor.execute(sql_s)
cursor.execute(sql_f)

res = cursor.fetchall()
# #
# for r in res:
#     print(r)

conn.close()
