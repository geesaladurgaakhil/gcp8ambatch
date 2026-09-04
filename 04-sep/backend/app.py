from flask import Flask, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Backend application is running",
        "platform": "Google Kubernetes Engine"
    })


@app.route("/api/message")
def message():

    hostname = socket.gethostname()

    return jsonify({
        "message": "Hello from Python backend running inside GKE!",
        "pod": hostname,
        "status": "success"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
