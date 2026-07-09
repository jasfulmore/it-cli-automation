import os
from core.backup import backup_files


def test_backup_files(tmp_path):
    # Create a fake source directory
    source = tmp_path / "source"
    source.mkdir()

    # Create a file inside it
    file = source / "hello.txt"
    file.write_text("Hello, World!")

    # Create backup destination
    backup_root = tmp_path / "backups"
    backup_root.mkdir()

    # Run the backup
    backup_files(str(source), str(backup_root))
    backups = list(backup_root.iterdir())

    assert len(backups) == 1

    backup_folder = backups[0]

    # Verify the copied file exists
    copied_file = backup_folder / "hello.txt"

    assert copied_file.exists()
    assert copied_file.read_text() == "Hello, World!"