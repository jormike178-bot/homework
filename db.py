
import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)

sql = conn.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, user_name TEXT, user_number);')

def register(user_id, user_name, user_number):
    sql.execute('INSERT INTO users VALUES (?, ?, ?);',(user_id, user_name, user_number))
    conn.commit()

def check_user(user_id):
    if sql.execute('SELECT * FROM users WHERE user_id = ?;', (user_id,)).fetchone():
        return True
    else:
        return False