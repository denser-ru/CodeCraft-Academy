# hub_node

## Описание

`hub_node` - это сервис, отвечающий за маршрутизацию узлов в рамках проекта CodeCraft-Academy. Он предоставляет API для регистрации новых узлов и получения списка доступных узлов.

## Техническое задание

**Статус:** В процессе реализации

[Полное техническое задание](TS.md)

## Текущее состояние

**Реализовано:**

*   Базовая структура приложения Flask.
*   Эндпоинт `/register_node` для регистрации узлов (POST).
*   Эндпоинт `/nodes` для получения списка узлов (GET).
*   Взаимодействие с базой данных SQLite.
*   Сборка Docker-образа.
*   Клонирование репозитория в Docker-контейнер при сборке.

**В работе:**

*   Реализация логирования.

**Планы:**

*   Добавить тесты.
*   Реализовать аутентификацию и авторизацию.

## Сборка и запуск

**Локальный запуск (для разработки):**

1. Клонируйте репозиторий и перейдите в директорию проекта:
    ```bash
    git clone https://github.com/denser-ru/CodeCraft-Academy.git
    cd CodeCraft-Academy/hub_node
    ```
2. Создайте и активируйте виртуальное окружение:
    ```bash
    python3 -m venv venv
    source venv/bin/activate # Linux/macOS
    venv\Scripts\activate # Windows
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Запустите приложение:
    ```bash
    python hub_node.py
    ```

**Запуск в Docker:**

1. Перейдите в директорию проекта:
    ```bash
    cd CodeCraft-Academy/hub_node
    ```
2. Соберите образ (используется базовый образ `python:3-slim-bullseye`):
    ```bash
    docker build -t hub-node .
    ```
3. Запустите контейнер:
    ```bash
    docker run -p 5000:5000 hub-node
    ```

## API

### `POST /register_node`

Регистрация нового узла.

**Запрос:**

```json
{
  "name": "node_1",
  "type": "trusted",
  "ip_address": "192.168.1.10",
  "port": 8080
}
```

**Ответ (успех, 201 Created):**

```json
{
  "id": "сгенерированный_uuid"
}
```

**Ответ (ошибка, 400 Bad Request):**

```json
{
  "error": "Необходимые параметры: name, type, ip_address, port"
}
```

**Ответ (ошибка, 409 Conflict):**

```json
{
  "error": "Имя узла уже занято"
}
```

**Ответ (ошибка, 500 Internal Server Error):**

```json
{
    "error": "Внутренняя ошибка сервера"
}
```

### `GET /nodes`

Получение списка зарегистрированных узлов.

**Запрос:**

(нет тела запроса)

**Ответ (успех, 200 OK):**

```json
[
  {"id": "uuid1", "type": "trusted"},
  {"id": "uuid2", "type": "local"}
]
```

## Примеры команд для тестирования

**1. Регистрация узла (успешная):**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "node_1", "type": "trusted", "ip_address": "192.168.1.10", "port": 8080}' http://localhost:5000/register_node
```

Ожидаемый ответ:

```json
{"id": "<сгенерированный_uuid>"}
```

**2. Регистрация узла (ошибка - отсутствие обязательных параметров):**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "node_2", "type": "local"}' http://localhost:5000/register_node
```

Ожидаемый ответ:

```json
{"error": "Необходимые параметры: name, type, ip_address, port"}
```

**3. Регистрация узла (ошибка - дублирование имени):**

*   Сначала зарегистрируйте узел с именем `node_3`:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "node_3", "type": "trusted", "ip_address": "192.168.1.20", "port": 9000}' http://localhost:5000/register_node
    ```
*   Затем попытайтесь зарегистрировать узел с тем же именем:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"name": "node_3", "type": "local", "ip_address": "192.168.1.30", "port": 7000}' http://localhost:5000/register_node
    ```

Ожидаемый ответ:

```json
{"error": "Имя узла уже занято"}
```

**4. Получение списка узлов (есть зарегистрированные узлы):**

```bash
curl http://localhost:5000/nodes
```

Ожидаемый ответ (пример):

```json
[
  {"id": "uuid1", "type": "trusted"},
  {"id": "uuid2", "type": "local"}
]
```

**5. Получение списка узлов (нет зарегистрированных узлов):**

```bash
curl http://localhost:5000/nodes
```

Ожидаемый ответ:

```json
[]
```

## Используемые технологии

*   Python 3 (базовый образ `python:3-slim-bullseye` для Docker)
*   Flask
*   SQLite
*   Docker
*   Git
*   GitHub

## Структура проекта

```
hub_node/
├── hub_node.py     # Основной код приложения
├── requirements.txt # Зависимости
├── Dockerfile       # Dockerfile для сборки образа
├── README.md        # Этот файл
└── TS.md            # Техническое задание
```

## Вклад в проект

(Информация о том, как внести вклад - пока не актуально)

## Лицензия

MIT License
