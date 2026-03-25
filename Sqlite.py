import sqlite3
import random
con = sqlite3.connect('data.db')
cur = con.cursor()
import Bank
data1 = Bank.self.accounts

cur.executemany(f"INSERT INTO Bank_Users(username, password, id)data1")
data = cur.execute("SELECT * FROM Bank_Users")
for row in data:
    print(row)
con.commit()
con.close()