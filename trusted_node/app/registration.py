import requests
import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

HUB_NODE_URL = os.environ.get('HUB_NODE_URL')

def register_on_hub():
    if not HUB_NODE_URL:
        logging.error("HUB_NODE_URL не определена в переменных окружения.")
        return

    node_name = os.environ.get('TRUSTED_NODE_NAME', 'trusted_node_default')
    node_type = os.environ.get('TRUSTED_NODE_TYPE', 'trusted')
    node_ip = os.environ.get('TRUSTED_NODE_IP', '127.0.0.1')
    node_port = os.environ.get('PORT', 5000)

    registration_data = {
        "name": node_name,
        "type": node_type,
        "ip_address": node_ip,
        "port": int(node_port)
    }

    while True:
        try:
            response = requests.post(f"{HUB_NODE_URL}/register_node", json=registration_data)
            if response.status_code == 201:
                logging.info(f"Успешно зарегистрирован на хаб-ноде: {HUB_NODE_URL}")
                break
            elif response.status_code == 409:
                logging.info(f"Узел с именем {node_name} уже зарегистрирован на хаб-ноде. Продолжаю работу.")
                break  # Выходим из цикла, если узел уже зарегистрирован
            else:
                logging.error(f"Ошибка регистрации на хаб-ноде. Статус код: {response.status_code}, Сообщение: {response.text}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка подключения к хаб-ноде: {e}")

        logging.info("Повторная попытка регистрации через 10 секунд...")
        time.sleep(10)