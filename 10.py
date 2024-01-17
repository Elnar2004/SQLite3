import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('SELECT username, age FROM Users ORDER BY age DEASC')
results = cursor.fetchall()
for now in results:
    print(row)
connection.close()