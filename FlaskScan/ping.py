import subprocess

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
    {'host': '192.168.1.11', 'name': '8'},
    {'host': '192.168.1.12', 'name': '9'},
    {'host': '192.168.1.13', 'name': '10'},
]

def check_device_online(device):
    try:
        subprocess.check_call(['ping', '-c', '1', '-W', '1', device['host']], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{device['name']} ({device['host']}) is online")
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        print(f"{device['name']} ({device['host']}) is offline")

for device in devices:
    check_device_online(device)
