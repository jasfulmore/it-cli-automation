import argparse
import platform
from core.formatter import print_header

from cli.system_commands import run_system
from cli.service_commands import run_services
from cli.backup_commands import run_backup
from cli.user_commands import run_user
from core.logger import logger
import sys


"""
IT CLI Automation Toolkit

A command-line utility for retrieving system information,
performing network diagnostics, and automating common IT tasks.
"""



def build_parser():
    """Create and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="it-cli",
        description="IT Automation Toolkit"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )


   # system commands
    system_parser = subparsers.add_parser(
        "system",
        help="System information"
    )

    system_sub = system_parser.add_subparsers(
        dest="system_cmd",
        required=True
    )

    system_sub.add_parser(
        "info",
        help="Display system information"
    )

    system_sub.add_parser(
        "json",
        help="Display system information as JSON"
    )


    # service commands
    services_parser = subparsers.add_parser(
        "services",
        help="Network and service utilities"
    )

    services_sub = services_parser.add_subparsers(
        dest="services_cmd",
        required=True
    )

    services_sub.add_parser(
        "check",
        help="Check internet connection"
    )

    services_sub.add_parser(
        "status",
        help="Display network status"
    )

    services_sub.add_parser(
        "restart",
        help="Restart network service"
    )


    # backup
    backup_parser = subparsers.add_parser(
        "backup",
        help="Backup files or folders"
    )

    backup_parser.add_argument(
        "source",
        help="File or folder to back up"
    )

    backup_parser.add_argument(
        "destination",
        help="Backup destination"
    )


    # user commands
    user_parser = subparsers.add_parser(
        "user",
        help="User information"
    )

    user_sub = user_parser.add_subparsers(
        dest="user_cmd",
        required=True
    )

    user_sub.add_parser(
        "info",
        help="Display current user information"
    )

    return parser


def main():
    """Run the CLI application."""
    print_header()

    parser = build_parser()
    args = parser.parse_args()
    logger.info("Command Executed: %s", " ".join(sys.argv))

    if args.command == "system":
        logger.info("Retrieving system information")
        run_system(args.system_cmd)

    elif args.command == "services":
        logger.info("Running services")
        run_services(args.services_cmd)

    elif args.command == "backup":
        try:
            logger.info(
                "Starting backup from %s to %s",
                args.source,
                args.destination
            )

            run_backup(args.source, args.destination)

            logger.info("Backup completed successfully")

        except Exception:
            logger.exception("Backup failed")

    elif args.command == "user":
        run_user(args.user_cmd)


if __name__ == "__main__":
    main()