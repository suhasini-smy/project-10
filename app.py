### Step 1: app.py (Flask + WebSockets backend)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from chatbot import get_bot_response

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("user_message")
def handle_user_message(message):
    response = get_bot_response(message)
    emit("bot_response", response)

if __name__ == "__main__":
    socketio.run(app, debug=True)

