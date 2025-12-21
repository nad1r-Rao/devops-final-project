from flask import Flask
import socket
import redis
import os

app = Flask(__name__)

# CONNECT TO THE DATABASE SERVICE
# We use the hostname 'redis-service' which we will define in Kubernetes
db = redis.Redis(host='redis-service', port=6379, decode_responses=True)

@app.route('/')
def hello():
    # Get the Container ID (Hostname)
    container_id = socket.gethostname()
    
    # DATABASE LOGIC: Try to increment the visitor counter
    try:
        visits = db.incr('counter')
    except redis.exceptions.ConnectionError:
        visits = "<i>[Cannot connect to Database]</i>"

    return f"""
    <html>
    <body style="background-color:#1a1a1a; color:white; font-family:monospace; display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
        <div style="text-align:center; padding:40px; border:2px solid #00ff00; border-radius:10px; box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);">
            <h1 style="color:#00ff00; font-size:3em; margin-bottom:10px;">🚀 OPTI-AI MICROSERVICES</h1>
            
            <div style="margin:20px 0; padding:20px; background-color:#333; border-radius:5px;">
                <p>Database Status: <strong>CONNECTED</strong></p>
                <p>Total Visitors:</p>
                <h1 style="color:#ffff00; font-size:4em; margin:0;">{visits}</h1>
            </div>

            <div style="margin-top:30px; color:#888;">
                <p>Frontend Served by Pod:</p>
                <p style="color:#00ffff;">{container_id}</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
