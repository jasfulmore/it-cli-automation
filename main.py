import argparse
from service_tools import check_connection, check_status, restart_network
from system_info import get_os, get_memory, get_disk

def main():
    parser = argparse.ArgumentParser(description="IT Suppor1t CLI Toolkit")

    # Main subcommands
    subparsers = parser.add_subparsers(dest="command")

    # Info command
    info_parser = subparsers.add_parser("info", help="Show system information")

    # User commands
    user_parser = subparsers.add_parser("user", help="User management")
    user_sub = user_parser.add_subparsers(dest="action")
    user_sub.add_parser("add", help="Add a new user")
    user_sub.add_parser("delete", help="Delete a user")
    user_sub.add_parser("reset", help="Reset user password")
    user_sub.add_parser("info", help="Get user info")

    # System Info
    system_parser = subparsers.add_parser("system", help="System Info")
    system_sub = system_parser.add_subparsers(dest="action")
    system_sub.add_parser("getos", help="Get OS Info")
    system_sub.add_parser("memory", help="Get Memory")
    system_sub.add_parser("getdisk", help="Get Disk Space")


    # Service commands
    service_parser = subparsers.add_parser("service", help="Service operations")
    service_sub = service_parser.add_subparsers(dest="action")
    service_sub.add_parser("check", help="Check service status")
    service_sub.add_parser("restart", help="Restart networking")
    service_sub.add_parser("connection", help="Check connection")

    # Backup commands
    backup_parser = subparsers.add_parser("backup", help="Backup tools")
    backup_sub = backup_parser.add_subparsers(dest="action")
    backup_sub.add_parser("logs", help="Backup logs")
    backup_sub.add_parser("configs", help="Backup config files")

    args = parser.parse_args()
    print(args)

check_connection()
check_status(service_name="ssh")
restart_network(service_name="NetworkManager")
get

if __name__ == "__main__":
    main()