# 🛠️ IT Support CLI Automation Toolkit (Python)

This is a command-line tool built in Python for performing common IT support and system administration tasks. It’s designed to be beginner-friendly, modular, and easily extendable.

---

## 📌 Features

### ✅ System Info Commands
- View OS version and platform
- Display memory (RAM) usage
- Show disk usage and space available

### ✅ Service Management
- Check if a service is running
- Restart any system service (e.g., NetworkManager, SSH)
- Check network connectivity (e.g., DNS ping)

### ✅ Coming Soon
- User account creation and deletion
- Backup and archive logs or config files
- Log output to a `.log` file

---

## 💻 Technologies Used

- Python 3
- [psutil](https://pypi.org/project/psutil/) — system info like memory and disk
- `subprocess` — run Linux/Windows system commands
- `argparse` — build interactive CLI with subcommands

---

## 🚀 How to Run

### 1. Clone the project
```bash
git clone https://github.com/your-username/it-cli-toolkit.git
cd it-cli-toolkit

### 2. Install requirements
pip install psutil
Run the tool
python main.py --help

