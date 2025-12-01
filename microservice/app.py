from flask import Flask, Response
from prometheus_client import Gauge, generate_latest
import os, random

app = Flask(__name__)
file_path = "logs.txt"

# Prometheus metric
file_size_gauge = Gauge("file_size_bytes", "Size of the log file in bytes")

@app.route('/')
def home():
    return "CloudWatchdog Microservice Running"

@app.route('/write')
def write_log():
    with open(file_path, "a") as f:
        f.write("x" * random.randint(1000, 5000))
    return "Wrote random data"

@app.route('/metrics')
def metrics():
    size = os.path.getsize(file_path) if os.path.exists(file_path) else 0
    file_size_gauge.set(size)
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
