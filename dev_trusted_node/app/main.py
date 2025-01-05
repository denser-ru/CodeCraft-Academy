from flask import Flask
from .database import init_db

app = Flask(__name__)

# Инициализация базы данных при старте приложения
with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # порт можно поменять на нужный