from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import os

# Set your TV host like 192.168.1.50:5555
TV_HOST = os.environ.get("TV_HOST", "")

app = Flask(__name__)
CORS(app)


def adb(*args):
    if not TV_HOST:
        return 1, "TV_HOST not set"
    cmd = ["adb", "-s", TV_HOST, *args]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode, (proc.stdout + proc.stderr).strip()


@app.get("/ping")
def ping():
    code, out = adb("get-state")
    status = "ok" if code == 0 else "error"
    return jsonify({"status": status, "detail": out})


@app.post("/key/<code>")
def key(code):
    code = code.strip().upper()
    rc, out = adb("shell", "input", "keyevent", code)
    status = "ok" if rc == 0 else "error"
    return jsonify({"status": status, "detail": out})


if __name__ == "__main__":
    # Run on all interfaces so your phone can reach it.
    app.run(host="0.0.0.0", port=8787)
