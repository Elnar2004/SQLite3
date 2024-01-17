import sqlite3
cursor = connection.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, usernsme TEXT NOT NULL, email TEXT NOT NULL, age INTEGER)''')
connection.commit()
connection.close()