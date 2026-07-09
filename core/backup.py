import datetime
import os
import shutil


def backup_files(source_dir, backup_dir):
    """
    Copy an entire directory into a timestamped backup folder.

    Args:
        source_dir (str): Directory to back up.
        backup_dir (str): Destination for backups.

    Returns:
        str: Path to the created backup folder.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        OSError: If the backup cannot be created.
    """

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    backup_folder = os.path.join(
        backup_dir,
        f"backup_{timestamp}"
    )

    shutil.copytree(source_dir, backup_folder)

    return backup_folder