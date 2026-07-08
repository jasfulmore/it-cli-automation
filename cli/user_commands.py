import getpass
import os



def run_user(command):
    # handles user related commands

    if command == "info":
        print("\n===== User Information =====")
        print(f"Current User      : {getpass.getuser()}")
        print(f"Home Directory    : {os.path.expanduser('~')}")
        print(f"Working Directory : {os.getcwd()}")

    else:
        print("Unknown User Command")


