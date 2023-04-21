import sqlite3

conn = sqlite3.connect('rescind_bot.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE rescind_counter
                    (id INTEGER PRIMARY KEY,
                    name TEXT,
                    counter INTEGER)''')

conn.commit()
conn.close()