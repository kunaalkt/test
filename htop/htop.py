from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/htop', methods=['GET'])
def htop():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = {
        "total": memory.total,
        "available": memory.available,
        "used": memory.used,
        "percent": memory.percent
    }

    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            process_info = proc.info
            processes.append(process_info)
        except psutil.NoSuchProcess:
            pass

    data = {
        "cpu_percent": cpu_percent,
        "memory": memory_usage,
        "processes": processes
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)