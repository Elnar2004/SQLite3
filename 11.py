import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute(''' SELECT username, age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ? ORDER BY age DESC ''', (30,))
results = cursor.fetchall()
for row in results:
    print(row)
connection.close()