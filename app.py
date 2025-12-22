from flask import Flask, request, redirect, url_for, render_template_string
from prometheus_flask_exporter import PrometheusMetrics # <--- NEW IMPORT
import socket
import redis
import os

app = Flask(__name__)

# INSTRUMENTATION: Automatically metrics for every page load
metrics = PrometheusMetrics(app) # <--- THIS ENABLED GRAFANA TALKING

# CONNECT TO REDIS MICROSERVICE
db = redis.Redis(host='redis-service', port=6379, decode_responses=True)

@app.route('/')
def index():
    pod_id = socket.gethostname()
    try:
        tasks = db.lrange('todo_tasks', 0, -1)
        db_status = "ONLINE 🟢"
    except redis.exceptions.ConnectionError:
        tasks = []
        db_status = "OFFLINE 🔴"

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>OptiAI Task Manager</title>
        <style>
            body { background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
            .container { background-color: #1e1e1e; padding: 40px; border-radius: 12px; box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5); width: 400px; text-align: center; border: 1px solid #333; }
            h1 { color: #bb86fc; margin-bottom: 20px; font-weight: 300; letter-spacing: 2px; }
            .status-box { background: #2c2c2c; padding: 15px; border-radius: 8px; margin-bottom: 20px; font-size: 0.9em; display: flex; justify-content: space-between; }
            .badge { padding: 4px 8px; border-radius: 4px; font-weight: bold; font-size: 0.8em; }
            .badge-blue { background: #03dac6; color: #000; }
            input[type="text"] { width: 70%; padding: 10px; border-radius: 4px; border: none; background: #333; color: white; outline: none; }
            button { width: 25%; padding: 10px; background-color: #bb86fc; color: #000; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; transition: 0.3s; }
            button:hover { background-color: #9955e8; }
            ul { list-style: none; padding: 0; margin-top: 20px; text-align: left; }
            li { background: #2c2c2c; padding: 10px; border-bottom: 1px solid #333; display: flex; justify-content: space-between; align-items: center; }
            li:first-child { border-top-left-radius: 8px; border-top-right-radius: 8px; }
            li:last-child { border-bottom-left-radius: 8px; border-bottom-right-radius: 8px; border-bottom: none; }
            .delete-btn { background: transparent; color: #cf6679; width: auto; padding: 0 5px; font-size: 1.2em; }
            .delete-btn:hover { background: transparent; color: #ff0000; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>OPTI-AI MANAGER</h1>
            
            <div class="status-box">
                <span>Backend DB: <strong>{{ db_status }}</strong></span>
            </div>
            <div class="status-box">
                <span>Served By Pod: <span class="badge badge-blue">{{ pod_id }}</span></span>
            </div>

            <form action="/add" method="POST">
                <input type="text" name="task" placeholder="New Microservice Task..." required>
                <button type="submit">ADD</button>
            </form>

            <ul>
                {% for task in tasks %}
                <li>
                    {{ task }}
                    <a href="/delete/{{ task }}" class="delete-btn">&times;</a>
                </li>
                {% else %}
                <li style="text-align:center; color:#666;">No tasks in Database...</li>
                {% endfor %}
            </ul>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, tasks=tasks, pod_id=pod_id, db_status=db_status)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        db.lpush('todo_tasks', task)
    return redirect(url_for('index'))

@app.route('/delete/<task>')
def delete(task):
    db.lrem('todo_tasks', 0, task)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
