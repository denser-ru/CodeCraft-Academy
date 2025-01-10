from flask import Flask
from database import init_db
import os

app = Flask(__name__)

# Получаем порт из переменной окружения PORT, если она установлена, иначе используем 5000
port = int(os.environ.get('PORT', 5000))

# Инициализация базы данных при старте приложения
with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)