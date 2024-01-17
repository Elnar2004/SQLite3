
import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('SELECT username, age FROM Users WHERE age > ?', (25,))
results = cursor.fetchall()
for row in results:
    print(row)
connection.close()