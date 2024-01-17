import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchall()[0]
print('ОБщее количество пользователей:', total_users)
connection.close()
