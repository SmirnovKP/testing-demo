import sqlite3
def get_users(conn):
    return conn.execute("SELECT name FROM users").fetchall()
def add_user(conn, name):
    conn.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
def create_users_table(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS users (name TEXT)")
    conn.commit()
