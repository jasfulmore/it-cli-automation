import platform
from config import APP_NAME, VERSION, AUTHOR


def print_header():
    """Display the application header."""

    print(
        f"""
====================================
        {APP_NAME}
====================================
Version : {VERSION}
Platform: {platform.system()}
Author:   {AUTHOR}

"""
    )