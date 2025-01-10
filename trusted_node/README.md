# Trusted Node

Это доверенный узел для проекта CodeCraft-Academy.

## Описание

Этот узел отвечает за ... (дополнить по мере разработки)

## Зависимости

- Python 3
- Flask
- requests
- SQLite
- python-dotenv

## Сборка и запуск (Docker)

1. Соберите Docker-образ:
   ```bash
   docker build -t trusted_node .
   ```
2. Запустите Docker-контейнер:
   ```bash
   docker run -d -p <желаемый_порт>:5000 --name trusted_node \
       -v $(pwd)/dbdata:/dbdata \
       -e HUB_NODE_URL="http://<адрес_хаб_ноды>:5000" \
       -e TRUSTED_NODE_NAME="my_trusted_node" \
       -e TRUSTED_NODE_TYPE="trusted" \
       -e TRUSTED_NODE_IP="<ip_адрес_trusted_node>" \
       trusted_node
   ```
   Обратите внимание на переменные окружения:
   - `HUB_NODE_URL`: URL адрес хаб-ноды.
   - `TRUSTED_NODE_NAME`: Имя этого доверенного узла.
   - `TRUSTED_NODE_TYPE`: Тип узла (например, "trusted").
   - `TRUSTED_NODE_IP`: IP-адрес этого доверенного узла.

## Запуск без Docker (для разработки)

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Перейдите в корневую директорию проекта `trusted_node`:
   ```bash
   cd trusted_node
   ```
3. Создайте файл `.env` в корне проекта и добавьте необходимые переменные окружения:
    ```
    PORT=8080
    HUB_NODE_URL="http://localhost:5000" # Замените на адрес локально запущенной hub-node
    TRUSTED_NODE_NAME="my_local_trusted_node"
    TRUSTED_NODE_TYPE="trusted"
    TRUSTED_NODE_IP="127.0.0.1"
    ```
4. Запустите приложение:
   ```bash
   python app/main.py
   ```

## TODO

Смотрите файл `TODO.md`.