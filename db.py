import sqlite3
from datetime import datetime

conn = sqlite3.connect('scrapped_dog_img.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS dogs_urls (
             id INTEGER PRIMARY KEY,
             url TEXT,
             created_at TEXT,
             updated_at TEXT)''')

c.execute('''INSERT INTO dogs_urls (url, created_at) VALUES (?, ?)''', ("www.google.com", datetime.now()))
conn.commit()

c.execute('''SELECT * FROM dogs_urls''')
results = c.fetchall()
print(results)