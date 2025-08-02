# SQL Injection Automation Scripts

This repository contains two Python scripts designed for educational and penetration testing purposes. They are used to detect possible SQL injection vulnerabilities through automated POST requests.

> ⚠️ **Legal Disclaimer**: These scripts are provided for **educational** and **ethical testing** only. Do **not** use them against systems you do not own or have explicit authorization to test.

---

## 📁 Files Included

### 1. `sqli_bruteforce.py`

This script reads a list of SQL injection payloads from a `payload.txt` file and sends them one by one to the target web application via POST requests. It prints out the payloads that might have bypassed authentication or triggered a different response.

#### Features:
- Reads payloads from file
- Sends custom HTTP headers
- Checks for anomalies in the response
- Useful for detecting simple SQLi vulnerabilities

#### Usage:
```bash
python3 sqli_bruteforce.py
```

Make sure the file `payload.txt` exists in the same directory and contains one payload per line.

---

### 2. `sqli_single_test.py`

This script performs a single SQL injection test using hardcoded credentials (`admin` / `pass`) and reports whether the attempt was successful or not based on the response content.

#### Features:
- Sends a single POST request with SQLi attempt
- Simple and lightweight
- Useful for quickly checking a single payload

#### Usage:
```bash
python3 sqli_single_test.py
```

---

## ⚙️ Requirements

- Python 3.x
- [`requests`](https://pypi.org/project/requests/) module  
Install with:
```bash
pip install requests
```

---

## 🧪 Target Setup

These scripts are designed to work with a vulnerable web app such as [bWAPP](http://www.itsecgames.com/) or DVWA hosted locally or in a lab environment like TryHackMe or HackTheBox.

- Example target: `http://10.10.30.130/sqli_3.php`
- Make sure the target accepts POST data with `login`, `password`, and `form` fields.
- Security level should be set to `low` (`security_level=0`).

---

## 🔐 Headers and Cookies

The scripts use custom headers to simulate a browser request. They also include cookies to maintain session and bypass security filters.

Modify the `headers` dictionary in the script if your session ID or host is different.

---

## 📌 Example Payload (in `payload.txt`)

```
admin' --
' or '1'='1
admin' OR 1=1 --
```

---

## 🙏 Credits

Developed for learning purposes by security enthusiasts. Inspired by common practices in offensive security training and CTFs.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more info.
