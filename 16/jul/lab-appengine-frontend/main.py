import os
import requests
from flask import Flask, render_template, request
import google.auth.transport.requests
import google.oauth2.id_token

app = Flask(__name__)

BACKEND_URL = os.environ.get(
    "BACKEND_URL",
    "https://backend-login-api-xxxxxxxx-uc.a.run.app/login"
)


def get_id_token(audience):
    """Fetch a Google-signed identity token for the given audience (Cloud Run URL)."""
    auth_req = google.auth.transport.requests.Request()
    return google.oauth2.id_token.fetch_id_token(auth_req, audience)


@app.route("/", methods=["GET", "POST"])
def login():
    message = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            token = get_id_token(BACKEND_URL)
            headers = {"Authorization": f"Bearer {token}"}

            resp = requests.post(
                BACKEND_URL,
                json={"username": username, "password": password},
                headers=headers,
                timeout=5
            )
            message = resp.json().get("message")
        except Exception as e:
            message = f"Error contacting backend: {e}"

    return render_template("login.html", message=message)


if __name__ == "__main__":