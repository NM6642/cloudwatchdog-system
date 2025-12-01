from flask import Flask, request

app = Flask(__name__)

LOG_FILE = "/app/logs.txt"

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if data.get("alertname") == "FileSizeTooLarge":
        # Truncate log
        with open(LOG_FILE, "w") as f:
            pass
        print("Log file truncated!")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
