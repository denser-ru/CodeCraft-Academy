import sqlite3
import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = 'hub_node.db'

# Функции для работы с базой данных
def get_db():
    db = sqlite3.connect(DATABASE)
    db.execute('''
        CREATE TABLE IF NOT EXISTS nodes (
            id TEXT PRIMARY KEY,
            name TEXT UNIQUE,
            type TEXT,
            ip_address TEXT,
            port INTEGER
        )
    ''')
    db.commit()
    return db

def add_node(node_data):
    db = get_db()
    node_id = str(uuid.uuid4())
    try:
        db.execute("INSERT INTO nodes VALUES (?, ?, ?, ?, ?)",
                   (node_id, node_data['name'], node_data['type'],
                    node_data['ip_address'], node_data['port']))
        db.commit()
        return node_id
    except sqlite3.IntegrityError:
        return None

def get_all_nodes():
    db = get_db()
    cursor = db.execute("SELECT id, type FROM nodes")
    nodes = [{'id': row[0], 'type': row[1]} for row in cursor.fetchall()]
    return nodes

# Эндпоинты API
@app.route('/register_node', methods=['POST'])
def register_node():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'type', 'ip_address', 'port')):
        return jsonify({'error': 'Необходимые параметры: name, type, ip_address, port'}), 400

    node_id = add_node(data)
    if node_id:
        return jsonify({'id': node_id}), 201
    else:
        return jsonify({'error': 'Имя узла уже занято'}), 409

@app.route('/nodes', methods=['GET'])
def list_nodes():
    nodes = get_all_nodes()
    return jsonify(nodes), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Запуск на порту 5000 для удобства тестирования