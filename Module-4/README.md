# Module 4: File, OS & Error Handling 📁⚙️🐍

This module focuses on working with files, operating system resources, and handling errors safely.
These skills are critical for DevOps automation, where scripts must interact with files, directories, logs, and handle failures gracefully.

## 🎯 Module Goals

By the end of this module, you will be able to:
- Read and write different file formats
- Manage files and directories using Python
- Handle runtime errors safely
- Implement logging for visibility and debugging
- Build a real-world automation script with error handling

---

## 1️⃣ Reading and Writing Files

Python provides built-in support for working with files.

### 🔁 Text Files

**🔹 Writing to a Text File**
```python
with open("example.txt", "w") as file:
    file.write("Hello DevOps\n")
```

**🔹 Reading from a Text File**
```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

### 🔁 CSV Files

CSV files are commonly used for reports and data exchange.

**🔹 Writing to a CSV File**
```python
import csv

data = [
    ["server", "status"],
    ["web-1", "running"],
    ["db-1", "stopped"]
]

with open("servers.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
```

**🔹 Reading from a CSV File**
```python
with open("servers.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

### 🔁 JSON Files

JSON is widely used in APIs and configuration files.

**🔹 Writing JSON Data**
```python
import json

config = {
    "app": "web-service",
    "port": 8080,
    "debug": True
}

with open("config.json", "w") as file:
    json.dump(config, file, indent=4)
```

**🔹 Reading JSON Data**
```python
with open("config.json", "r") as file:
    data = json.load(file)
    print(data)
```

### 🛠 DevOps Use Case
- Read configuration files
- Store reports and logs
- Process API and cloud metadata

---

## 2️⃣ Directory & File Management (os, shutil)

Python provides modules to interact with the operating system.

**🔹 Working with os**
```python
import os

print(os.getcwd())
os.mkdir("logs")
print(os.listdir("."))
```

**🔹 Checking File and Directory Existence**
```python
if os.path.exists("config.json"):
    print("Config file exists")
```

**🔹 Working with shutil**
```python
import shutil

shutil.copy("example.txt", "backup_example.txt")
shutil.move("backup_example.txt", "backup/")
```

### 🛠 DevOps Use Case
- Manage log directories
- Organize backups
- Automate file operations

---

## 3️⃣ Exception Handling (try, except, finally)

Exception handling prevents scripts from crashing unexpectedly.

**🔹 Basic try–except**

```python
try:
    file = open("missing.txt", "r")
except FileNotFoundError:
    print("File not found")
```

**🔹 Handling Multiple Exceptions**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(e)
```

**🔹 Using finally**
```python
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("Error opening file")
finally:
    print("Execution completed")
```

### 🛠 DevOps Use Case

- Prevent pipeline failures
- Handle network or file errors
- Ensure cleanup steps always run

---

## 4️⃣ Logging & Basic Debugging

Logging provides insight into script execution.

**🔹 Basic Logging Setup**
```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.error("An error occurred")
```

**🔹 Logging with Exception Handling**
```python
try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Division by zero error")
```

### 🛠 DevOps Use Case

- Track automation execution
- Debug failures
- Maintain audit logs

---

## 🚀 Project: Backup Automation Script

**📌 Project Description**

Develop a Python script that:
- Backs up files or directories
- Handles errors gracefully
- Logs all actions and failures

**🔹 Sample Logic**
```python
import os
import shutil
import logging

source = "data/"
destination = "backup/"

try:
    if not os.path.exists(destination):
        os.mkdir(destination)

    shutil.copytree(source, destination, dirs_exist_ok=True)
    logging.info("Backup completed successfully")

except Exception as e:
    logging.exception("Backup failed")

finally:
    print("Backup process finished")
```

---

## 🎯 Learning Outcomes

- Combine file handling, OS operations, and error handling
- Build production-ready automation scripts
- Improve reliability and observability

---
