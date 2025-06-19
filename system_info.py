import platform
import psutil

def get_os():
    os = platform.platform()
    print(f"OS and Version: {os}")

get_os()



def get_memory():
    comp_memory = psutil.virtual_memory()

    convert_gb = comp_memory.total / (1024**3)
    return convert_gb

print(f"Total Memory: {get_memory():.2f} GB")

get_memory()


def get_disk(drive_letter):
    
    try:
        mem = psutil.disk_usage(drive_letter)

        all_space = mem.total / (1024**3)
        used_space = mem.used / (1024**3)
        free_space = mem.free / (1024**3)
        percent_used = mem.percent

        print(f"Disk Info For {drive_letter}: ")
        print(f"Total Space: {all_space:.2f} GB")
        print(f"Used Space: {used_space:.2f} GB")
        print(f"Space Avaiable: {free_space:.2f} GB")
        print(f"Percentage of Space Used: {percent_used}%")

    except FileNotFoundError:
        print(f"Error: Driver {drive_letter} Not Found.")
    except Exception as e:
        print(f"An Error Has Occured.")

get_disk(drive_letter="C:")

