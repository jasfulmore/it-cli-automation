import json
from core.system_info import get_system_info


def run_system(command):
    # handles all system cli commands
    
    data = get_system_info()

    if command == "info":
        print("\n===== System Information =====")
        print(f"OS: {data['os']}")
        print(f"Memory: {data['memory']:.2f} GB")

        disk = data["disk"]

        print("\n===== Disk Information =====")
        print(f"Total: {disk['total']:.2f} GB")
        print(f"Used : {disk['used']:.2f} GB")
        print(f"Free : {disk['free']:.2f} GB")
        print(f"Usage: {disk['percent']}%")

    elif command == "json":
        print(json.dumps(data, indent=4))