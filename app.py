from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # This grabs the unique ID of the specific container running this request
    container_id = socket.gethostname()
    
    return f"""
    <html>
    <body style="background-color:#1a1a1a; color:white; font-family:monospace; display:flex; justify-content:center; align-items:center; height:100vh; margin:0;">
        <div style="text-align:center; padding:40px; border:2px solid #00ff00; border-radius:10px; box-shadow: 0 0 20px rgba(0, 255, 0, 0.2);">
            <h1 style="color:#00ff00; font-size:3em; margin-bottom:10px;">🚀 OPTI-AI DEVOPS</h1>
            <h2 style="border-bottom: 1px solid #555; padding-bottom:20px;">SYSTEM OPERATIONAL</h2>
            
            <div style="margin:30px 0; font-size:1.2em;">
                <p>Request Handled By Container ID:</p>
                <h1 style="color:#ff00ff; font-size:2.5em; margin:10px;">{container_id}</h1>
            </div>

            <p style="color:#888;">Refresh this page to see Kubernetes Load Balancing in action!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
