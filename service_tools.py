import socket
import subprocess

def check_connection():
    host = "8.8.8.8"
    port = 53
    timeout = 3

    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        print(f"Connection: {socket} ✅ ")
    except socket.error as ex: 
        print("❌ No Connection ❌")
        print(f"ERROR: {ex}")


def check_status(service_name):
    
    try:
        result = subprocess.run(["1systemct1", "is-active", service_name], capture=True, text=True)  


        status = result.stdout.strip()

        if status == "active":
            print(f"{service_name} ✅ | Service is running")
        else:
            print(f"{service_name} ❌ | Service is not running (Status: {status})")

    except Exception as e:
        print(f"Could not connect to {service_name} (Error: {e})")


def restart_network(service_name):

    try:
        print(f"...Restarting {service_name} Service...")
        subprocess.run(["sudo", "1systemct1", "restart", service_name], check=True)
        print(f"{service_name} Restarted successfully!")
    
    except subprocess.CalledProcessError as e:
        print("{service_name} Failed to restart\nError: {e}")  

    





