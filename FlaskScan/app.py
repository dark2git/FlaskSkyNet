from flask import Flask, render_template, jsonify
import subprocess

app = Flask(__name__)

devices = [
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.2', 'name': 'laptop'},
    {'host': '192.168.1.3', 'name': 'printer'},
    {'host': '192.168.1.4', 'name': '1'},
    {'host': '192.168.1.5', 'name': '2'},
    {'host': '192.168.1.6', 'name': '3'},
    {'host': '192.168.1.7', 'name': '4'},
    {'host': '192.168.1.8', 'name': '5'},
    {'host': '192.168.1.9', 'name': '6'},
    {'host': '192.168.1.10', 'name': '7'},
    {'host': '192.168.1.11', 'name': 'Huawei'},
    {'host': '192.168.1.12', 'name': '9'},
    {'host': '192.168.1.13', 'name': '10'},
    {'host': '192.168.1.14', 'name': '11'},
    {'host': '192.168.1.15', 'name': '12'},
    {'host': '192.168.1.113', 'name': 'rasp'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
    {'host': '192.168.1.1', 'name': 'router'},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_devices')
def check_devices():
    status_text = ""
    for device in devices:
        try:
            subprocess.check_call(['ping', '-c', '1', '-W', '1', device['host']], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            status_text += f"{device['name']} ({device['host']}) is online<br>"
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
            status_text += f"{device['name']} ({device['host']}) is offline<br>"
    return status_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
