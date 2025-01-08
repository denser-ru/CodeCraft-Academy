import sqlite3
from flask import g
import os

# Путь для Docker
DOCKER_DATABASE = '/dbdata/trusted_node.db'
# Путь для локального запуска (в корне проекта)
LOCAL_DATABASE = 'trusted_node.db'

DATABASE = DOCKER_DATABASE if os.environ.get('RUNNING_IN_DOCKER') else LOCAL_DATABASE

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
    # Проверяем, существует ли файл схемы
    schema_file = 'schema.sql'
    if os.path.exists(schema_file):
        with open(schema_file, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()