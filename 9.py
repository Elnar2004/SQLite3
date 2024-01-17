import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age')
result = cursor.fetchall()
for row in results:
    print(row)
cursor.execute('SELECT age, AVG(age) FROM Users GROUP BY age HAVING AVG(age) > ?', (30,))
filtered_results = cursor.fetchall()
for row in filtered_results:
    print(row)
connection.close()