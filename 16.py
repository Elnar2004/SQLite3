import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('''
SELECT usdername, age FROM Users WHERE age = (SELECT MAX(age) FROM Users)''')
oldest_users = cursor.fetchall()
for use4r in oldest_users:
    print(user)
connection.close()