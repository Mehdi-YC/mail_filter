import sqlite3
conn = sqlite3.connect("mails.db")
conn.row_factory = lambda cursor, row: row[0]
cur = conn.cursor()
cur.execute('delete from mails')
conn.commit()