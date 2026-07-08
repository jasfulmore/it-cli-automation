from core.backup import backup_files


def run_backup(source, destination):
    # handles running file backups

    try:
        backup_files(source. destination)
        print("Backup Completed Successfully")
    except Exception as e:
        print(f"Backup Failed: {e}")