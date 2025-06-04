from flask import Flask, request, jsonify, render_template, redirect, url_for

import tasks

app = Flask(__name__)

# HTML interface
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks.load_tasks(), points=tasks.load_points())

@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify(tasks.load_tasks())

@app.route('/tasks', methods=['POST'])
def add_task():
    if request.is_json:
        data = request.get_json(silent=True) or {}
        name = data.get('name')
        if not name:
            return jsonify({'error': 'name required'}), 400
        points = int(data.get('points', 10))
        tasks.add_task(name, points)
        return jsonify({'message': 'task added'}), 201
    # form submission from HTML
    name = request.form.get('name')
    if not name:
        return redirect(url_for('index'))
    points = int(request.form.get('points', 10))
    tasks.add_task(name, points)
    return redirect(url_for('index'))

@app.route('/tasks/<int:task_id>/done', methods=['POST'])
def mark_done(task_id):
    tasks.mark_done(task_id)
    if request.is_json:
        return jsonify({'message': 'task marked done'})
    return redirect(url_for('index'))

@app.route('/points', methods=['GET'])
def show_points():
    return jsonify({'points': tasks.load_points()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
