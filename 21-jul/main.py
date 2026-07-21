import os
import json
from flask import Flask, request, jsonify
from google.cloud import tasks_v2

app = Flask(__name__)

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION = "us-central1"
QUEUE_NAME = "my-lab-queue"

client = tasks_v2.CloudTasksClient()


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "App is running"}), 200


# ---------- TASK QUEUE DEMO ----------

@app.route("/add-task", methods=["GET"])
def add_task():
    """Creates a task that will later call /process-task"""
    parent = client.queue_path(PROJECT_ID, LOCATION, QUEUE_NAME)

    task = {
        "app_engine_http_request": {
            "http_method": tasks_v2.HttpMethod.POST,
            "relative_uri": "/process-task",
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"message": "Hello from a queued task!"}).encode()
        }
    }

    response = client.create_task(parent=parent, task=task)
    return jsonify({"status": "Task created", "task_name": response.name}), 200


@app.route("/process-task", methods=["POST"])
def process_task():
    """This is called asynchronously by Cloud Tasks"""
    data = request.get_json(silent=True) or {}
    print(f"Processing task with payload: {data}")
    return jsonify({"status": "Task processed", "received": data}), 200


# ---------- CRON JOB DEMO ----------

@app.route("/cron/cleanup", methods=["GET"])
def cron_cleanup():
    """This endpoint is hit automatically by App Engine's cron scheduler"""
    print("Running scheduled cleanup job...")
    return jsonify({"status": "Cleanup job executed"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)