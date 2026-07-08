import platform
import psutil
import os



def get_os():
    return platform.platform()


def get_memory():
    return psutil.virtual_memory().total / (1024 ** 3)


def get_disk(drive_letter):
    try:
        usage = psutil.disk_usage(drive_letter)

        return {
            "total": usage.total / (1024 ** 3),
            "used": usage.used / (1024 ** 3),
            "free": usage.free / (1024 ** 3),
            "percent": usage.percent
        }
    
    except FileNotFoundError:
        return None


def get_system_info():
    return {
     
        "os": get_os(),
        "memory": get_memory(),
        "disk": get_disk("C:" if os.name == "nt" else "/")
    }

