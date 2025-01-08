# Используем легковесный образ Python 3
FROM python:3-slim-buster

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения в контейнер
COPY app/ .

# Создаем файл базы данных
RUN touch trusted_node.db

# Монтируем директорию с базой данных, что бы данные сохранялись
VOLUME ["/dbdata"]

# Устанавливаем переменную окружения PORT
ENV PORT=5000

# Запускаем приложение при старте контейнера (прямой запуск скрипта)
CMD ["python", "main.py"]