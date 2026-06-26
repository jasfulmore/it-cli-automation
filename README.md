# 🧰 IT CLI Automation Toolkit

A Python-based command-line automation toolkit designed to simplify system diagnostics, service monitoring, and basic IT operations through a unified CLI interface.

This project focuses on **automation engineering, system tooling, and CLI architecture design**.

---

## 🚀 Features

### 💻 System Diagnostics
- Operating system detection
- Memory usage reporting (GB)
- Disk usage analysis (total, used, free, percent)
- Cross-platform support (Windows / Linux / macOS)

### 🌐 Network Utilities
- Network connectivity checks *(in progress)*
- Network status validation tools *(planned)*

### 🔧 Service Tools
- Service status checking *(in progress)*
- Network/service restart utility *(basic implementation)*

### 📦 CLI Interface
- Built with Python `argparse`
- Subcommand-based structure:
  - `system`
  - `services`
  - `backup` *(planned)*
  - `user` *(planned)*
- Modular architecture for scalability

---

## 🧠 Roadmap

### 🗂 Backup Automation
- File/folder backup system
- Scheduled backups (cron / task scheduler support)
- Compression (zip/tar)
- Cloud integration (AWS S3 / Google Drive API)

### 👤 User Management Tools
- Local user account inspection
- Permission/role checking
- Admin utilities

### 📊 Logging & Monitoring
- System logs
- Error tracking
- Export logs to file

### 🌐 Integration Layer
- REST API wrapper for system commands
- Webhook support
- JSON output mode for automation tools

### ⚙️ CLI Improvements
- Colored terminal output
- Interactive shell mode (`toolkit shell`)
- Config file support (`config.json`)
- Global installable CLI (`toolkit` command)

---

## 🛠 Tech Stack

- Python 3.x
- argparse
- psutil
- platform
- os
- subprocess

---

## 📂 Project Structure

it-cli-automation/
│── main.py
│── system_info.py
│── service_tools.py
│── README.md

---

## ▶️ Usage

### System Commands

```bash
python main.py system info
python main.py system disk
```

### Service Commands

```bash
python main.py services status
python main.py services restart
```


### Example Output
Running on: Windows

--- SYSTEM INFO ---
OS: Windows 11
Memory: 12.34 GB

--- DISK INFO ---
Total: 512 GB
Used: 300 GB
Free: 212 GB
Usage: 58.6%
