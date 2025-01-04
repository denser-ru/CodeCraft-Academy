import sqlite3
from flask import g

DATABASE = '/dbdata/trusted_node.db' # путь к монтируемому тому

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with open('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# Создадим пустой файл schema.sql, что бы не было ошибок
# В app/schema.sql пока добавим строку с комментарием
# -- Create the users table