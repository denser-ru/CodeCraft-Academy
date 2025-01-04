# Trusted Node

Это доверенный узел для проекта CodeCraft-Academy.

## Описание

Этот узел отвечает за ... (дополнить по мере разработки)

## Зависимости

- Python 3
- Flask
- requests
- SQLite

## Сборка и запуск

1. Соберите Docker-образ:
   ```bash
   docker build -t trusted_node .
   ```
2. Запустите Docker-контейнер:
   ```bash
   docker run -d -p 5000:5000 --name trusted_node -v $(pwd)/dbdata:/dbdata trusted_node
   ```
   (Обратите внимание на монтирование volume)

## TODO

Смотрите файл `TODO.md`.
