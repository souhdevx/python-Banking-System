import sqlite3

con = sqlite3.connect('bank_data.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT,
        id INTEGER PRIMARY KEY,
        balance REAL
    )
''')

def save_user(username, password, user_id, balance=0.0):
    cur.execute("INSERT INTO users VALUES (?, ?, ?, ?)", 
                (username, password, user_id, balance))
    con.commit()

con.close()
