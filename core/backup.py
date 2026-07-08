import shutil
import os
import datetime


def backup_files(source_dir, backup_dir):
    # Get the current date and time for naming the backup folder
    current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_folder = os.path.join(backup_dir, f"backup_{current_time}")
    
    try:
        # Create the backup directory
        os.makedirs(backup_folder)
        
        # Copy all files and subdirectories from source to backup folder
        shutil.copytree(source_dir, backup_folder)
        
        print(f"Backup successful! Files have been copied to {backup_folder}")
    
    except Exception as e:
        print(f"Error: {e}")

        