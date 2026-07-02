import argparse
import platform
from service_tools import check_connection, check_status, restart_network
from system_info import get_os, get_memory, get_disk
from backup import backup_files
import getpass
import os

def run_system():
    print("\n===== System Info =====")

    print("OS:", get_os())
    print(f"Memory: {get_memory():.2f} GB")

    if os.name == "nt":
        disk = get_disk("C:")
    else:
        disk = get_disk("/")

    if disk:
        print("\nDisk Info:")
        print(f"Total: {disk['total']:.2f} GB")
        print(f"Used: {disk['used']:.2f} GB")
        print(f"Free: {disk['free']:.2f} GB")
        print(f"Usage: {disk['percent']:.2f}%")



def check_services():
    while True:
        print("\n===== Service Tools =====")
        print("1. Check Internet Connection")
        print("2. Check Network Status")
        print("3. Restart Network")
        print("4. Back")

        choice = input("\nSelect an option: ")

        if choice == "1":
            check_connection()
        elif choice == "2":
            check_status()
        elif choice == "3":
            confirm = input("Are you sure you want to restart the network? (y/n): ").lower()

            if confirm == "y":
                restart_network()
        
        elif choice == "4":
            break
        else:
            print("Invalid Choice.")
        



def run_backup():
    print("\n===== Backup Tool =====")

    source = input("Enter the file or folder to back: ")
    destination = input("Enter the backup destination: ")

    try:
        backup_files(source, destination)
        print(f"\nBackup completed successfully")

    except Exception as e:
        print(f"\nBackup Failed: {e}")


def user_menu():
    while True:
        print("\n===== User Tools =====")
        print("1. Current User") 
        print("2. Current Working Directory") 
        print("3. Home Directory") 
        print("4. Back") 

        choice = input("\nChoose an option: ")

        if choice == "1":
            print(f"\nCurrent User: {getpass.getuser()}")
        elif choice == "2":
            print(f"\nWorking Directory: {os.getcwd()}")
        elif choice == "3":
            print(f"\nHome Directory: {os.path.expanduser('~')}")
        elif choice == "4":
            break

        else:
            print("Invalid Choice")
           


def main():
    OS = platform.system()
    print(f"Running on: {OS}")

    parser = argparse.ArgumentParser(description="IT Automation Toolkit")

    subparsers = parser.add_subparsers(dest="command")

    system_parser = subparsers.add_parser("system")
    services_parser = subparsers.add_parser("services")
    backup_parser = subparsers.add_parser("backup")
    user_parser = subparsers.add_parser("user")

    args = parser.parse_args()

    if args.command == "system":
        run_system()
    elif args.command == "services":
        check_services()
    elif args.command == "backup":
        run_backup()
    elif args.command == "user":
        user_menu()
    else:
        parser.print_help()
        

if __name__ == "__main__":
    main()