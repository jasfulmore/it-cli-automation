from core.backup import backup_files


def run_backup(source, destination):
    # handles running file backups

    try:
        location = backup_files(source, destination)
        print(f"Backup created successfully!")
        print(location)

    except Exception as e:
        print(f"Backup failed: {e}")