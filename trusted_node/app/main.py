from flask import Flask
from database import init_db
import os
from registration import register_on_hub
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные из .env файла

app = Flask(__name__)

# Получаем порт из переменной окружения PORT, если она установлена, иначе используем 5000
port = int(os.environ.get('PORT', 5000))

# Инициализация базы данных при старте приложения
with app.app_context():
    init_db()

# Регистрация на хаб-ноде при запуске
register_on_hub()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)