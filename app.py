from flask import Flask, render_template
from flask_socketio import SocketIO

import configs

app = Flask(__name__)
app.config.from_object(configs)

socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('send')
def chat(data):
    socketio.emit('get', data)


@socketio.on('test')
def test():
    socketio.send("test")


if __name__ == "__main__":
    socketio.run(app)
