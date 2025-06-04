from flask import Flask, request, jsonify

import tasks

app = Flask(__name__)

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks.load_tasks())

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json or {}
    name = data.get('name')
    if not name:
        return jsonify({'error': 'name required'}), 400
    points = int(data.get('points', 10))
    tasks.add_task(name, points)
    return jsonify({'message': 'task added'}), 201

@app.route('/tasks/<int:task_id>/done', methods=['POST'])
def mark_done(task_id):
    tasks.mark_done(task_id)
    return jsonify({'message': 'task marked done'})

@app.route('/points', methods=['GET'])
def show_points():
    return jsonify({'points': tasks.load_points()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
