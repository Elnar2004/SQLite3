import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('SELECT AVG(age FROM Users')
average_age = cursor.fetchall()[0]
print('Средний возраст пользователей:', average_age)
connection.close