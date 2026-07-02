from backup import backup_files
import getpass
import os



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
           