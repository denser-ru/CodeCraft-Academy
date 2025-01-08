# Trusted Node

Это доверенный узел для проекта CodeCraft-Academy.

## Описание

Этот узел отвечает за ... (дополнить по мере разработки)

## Зависимости

- Python 3
- Flask
- requests
- SQLite

## Сборка и запуск (Docker)

1. Соберите Docker-образ:
   ```bash
   docker build -t trusted_node .
   ```
2. Запустите Docker-контейнер:
   ```bash
   docker run -d -p <желаемый_порт>:5000 --name trusted_node -v $(pwd)/dbdata:/dbdata trusted_node
   ```
   Обратите внимание, что порт внутри контейнера по умолчанию 5000 (указан в `Dockerfile`), но вы можете отобразить его на любой порт хост-машины.

## Запуск без Docker (для разработки)

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Перейдите в корневую директорию проекта `trusted_node`:
   ```bash
   cd trusted_node
   ```
3. Запустите приложение как модуль:
   ```bash
   python -m app.main
   ```
   Вы можете указать порт, используя переменную окружения `PORT`:
   ```bash
   export PORT=8080
   python -m app.main
   ```
   Или запустить приложение с указанием переменной окружения в команде:
   ```bash
   PORT=8080 python -m app.main
   ```

## TODO

Смотрите файл `TODO.md`.