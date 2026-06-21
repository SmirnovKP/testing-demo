import sys
import sqlite3
from pathlib import Path
sys.path.append('..')
from app.repo import get_users, add_user, create_users_table

def test_create_users_table():
    db = Path("/tmp/test.db")
    conn = sqlite3.connect(db)
    create_users_table(conn)
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'").fetchone()
    assert result is not None
    conn.close()
    db.unlink()

def test_add_user():
    db = Path("/tmp/test.db")
    conn = sqlite3.connect(db)
    create_users_table(conn)
    add_user(conn, 'alice')
    users = get_users(conn)
    assert users == [('alice',)]
    conn.close()
    db.unlink()

def test_get_users_empty():
    db = Path("/tmp/test.db")
    conn = sqlite3.connect(db)
    create_users_table(conn)
    users = get_users(conn)
    assert users == []
    conn.close()
    db.unlink()
