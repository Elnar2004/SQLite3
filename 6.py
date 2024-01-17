import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('DELETE FROM Users WHERE username = ?', ('newuser'))
connection.commit()
connection.close()
