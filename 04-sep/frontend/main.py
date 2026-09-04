from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

BACKEND_URL = "http://34.71.60.217"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/backend")
def backend():

    try:

        response = requests.get(
            f"{BACKEND_URL}/api/message",
            timeout=10
        )

        response.raise_for_status()

        return jsonify(response.json())

    except requests.exceptions.RequestException as error:

        return jsonify({
            "status": "error",
            "message": str(error)
        }), 500


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080
    )
