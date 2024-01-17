import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(user)
connection.close()
