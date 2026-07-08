from core.service_tools import check_connection, check_status, restart_network



def run_services(command):
    # handles service cli commands

    if command == "check":
        check_connection()
    elif command == "status":
        check_status()
    elif command == "restart":
        restart_network()

    else:
        print("Unknown service command")