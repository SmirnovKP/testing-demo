import sys
import sqlite3
sys.path.append('../..')
from app.repo import get_users, add_user, create_users_table
def test_get_users_with_real_db(tmp_path):
    # Создаём временную базу данных
    db = tmp_path / "app.db"
    conn = sqlite3.connect(db)
    
    # Создаём таблицу и добавляем данные
    create_users_table(conn)
    add_user(conn, 'alice')
    add_user(conn, 'bob')
    
    # Проверяем
    users = get_users(conn)
    assert users == [('alice',), ('bob',)]
    
    conn.close()
def test_empty_db(tmp_path):
    db = tmp_path / "app.db"
    conn = sqlite3.connect(db)
    create_users_table(conn)
    
    users = get_users(conn)
    assert users == []
    
    conn.close()
