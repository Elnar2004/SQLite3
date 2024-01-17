import sqlite3
connection.close()
cursor = connection.cursor()
cursor.execute('CREATE INDEX idx_email ON Users (email)')
connection.commit()
connection.close()