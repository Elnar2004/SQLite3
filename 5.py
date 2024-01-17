import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('UPDATE Users SET age = ? WHERE username = ?', (29, 'newuser'))
connection.commit()
connection.close()