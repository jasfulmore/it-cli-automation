# IT CLI Automation Toolkit

A Python-based command-line application that automates common IT administration tasks such as retrieving system information, managing services, backing up files, and displaying user information.

## Features

- System information
- JSON output
- Service utilities
- Backup utility
- User information
- Logging
- Configurable application settings

## Technologies

- Python 3
- argparse
- logging
- pathlib
- psutil

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/it-cli-automation.git
cd it-cli-automation
pip install -r requirements.txt
```

## Usage

```bash
python main.py system info
```

```bash
python main.py system json
```

```bash
python main.py services check
```

```bash
python main.py backup source destination
```

```bash
python main.py user info
```

## Example Output

```text
====================================
IT CLI Automation Toolkit
====================================

Version : 1.0.0
Platform: macOS
```

## Project Structure

```text
it-cli-automation/
├── cli/
├── core/
├── logs/
├── tests/
├── config.py
├── main.py
└── requirements.txt
```

## Future Improvements

- Network diagnostics
- Process management
- GitHub Actions
- Pytest coverage
- CSV export

## Author

Jasmine Fulmore