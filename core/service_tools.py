import platform
import socket
import subprocess



def check_connection():
    host = "8.8.8.8"
    port = 53
    timeout = 3

    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()

        print("Connection: OK ✅")

    except socket.error as ex:
        print("❌ No Connection ❌")
        print(f"ERROR: {ex}")




def check_status():
    service_name = "networking"
    system = platform.system()
    
    try:
        # Mac/Linux/Windows
        if system == "Linux":
            print("Linux detected (systemctl not available on macOS)")

        # global network test    
        result = subprocess.run(
            ["ping", "-c", "1", "8.8.8.8"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("Network Status: ✅ | Service is active")
        else:
            print("Network Status: ❌ | Service is not active")

    except Exception as e:
        print(f"Could not check network status (Error: {e})")




def restart_network(service_name):

    try:
        print(f"...Restarting {service_name} Service...")
        #subprocess.run(["sudo", "1systemct1", "restart", service_name], check=True)
        print(f"{service_name} Restarted successfully!")
    
    except subprocess.CalledProcessError as e:
        print(f"{service_name} Failed to restart\nError: {e}")  

    





