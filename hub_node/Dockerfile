# Используем легковесный образ Python
FROM python:3-slim-bullseye

# Устанавливаем Git
RUN apt-get update && apt-get install -y git

# Устанавливаем рабочую директорию
WORKDIR /app

# Клонируем репозиторий из GitHub
RUN git clone -b dev_hub_node https://github.com/denser-ru/CodeCraft-Academy.git .

# Переходим в директорию проекта
WORKDIR /app/hub_node

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Открываем порт 5000
EXPOSE 5000

# Команда для запуска приложения
CMD ["python", "hub_node.py"]