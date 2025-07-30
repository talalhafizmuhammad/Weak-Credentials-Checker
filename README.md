# 🔐 SSH & Telnet Default Credential Tester

A Python script that attempts to log in to a target machine using a list of default or leaked credentials over:

- 🚪 **SSH** (`paramiko`)
- 📡 **Telnet** (`telnetlib`)

This tool is great for **penetration testing**, **red teaming**, or **hardening device security** by identifying weak or default login credentials.

---

## 📌 Features

- Reads credentials from a `defaults.txt` file
- Attempts **SSH login** on port 22
- Attempts **Telnet login** on port 23
- Gracefully handles timeouts, login failures, and unexpected responses
- Detailed output for each login attempt

---

## 🖥️ How to Use

### 1. Prepare a credentials file (`defaults.txt`)

Each line should be in one of the following formats:

