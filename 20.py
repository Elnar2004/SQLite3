import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('SELECT * FROM Usres WHERE age IS NULL')
unknown_age_users = cursor.fetchall()
for user in unknown_age_users:
    print(user)
connection.close()