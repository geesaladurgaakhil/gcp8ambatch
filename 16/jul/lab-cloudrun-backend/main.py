from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded "database" for the lab
VALID_USERS = {
    "admin": "password123"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if VALID_USERS.get(username) == password:
        return jsonify({"status": "success", "message": f"Welcome {username}!"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "Cloud Run backend is running"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)