# Module 5: Automation, Shell & APIs 🤖🔧🌐

This module focuses on automation in DevOps using Python, including executing shell commands, interacting with remote systems, and working with REST APIs.
These skills are fundamental for building real-world DevOps automation scripts that integrate systems, services, and cloud platforms.

## 🎯 Module Goals

By the end of this module, you will be able to:
- Understand automation concepts in DevOps
- Execute shell commands from Python
- Connect to remote systems using SSH
- Work with REST APIs
- Parse and process JSON responses
- Build automation workflows driven by API data
---
## 1️⃣ Automation Concepts for DevOps

Automation in DevOps aims to:
- Reduce manual work
- Improve reliability and consistency
- Speed up deployments and operations

**🔹 Common Automation Use Cases**

- Server provisioning
- Configuration management
- Monitoring and alerting
- CI/CD pipeline tasks
- Cloud resource management

**🔹 Why Python for Automation?**

- Easy to write and maintain
- Strong ecosystem of libraries
- Works across platforms
- Excellent integration with DevOps tools

---

## 2️⃣ Running Shell Commands with Python

Python can execute system commands using built-in and third-party libraries.

**🔹 Using subprocess**
```python
import subprocess

result = subprocess.run(
    ["ls", "-l"],
    capture_output=True,
    text=True
)

print(result.stdout)
```

**🔹 Handling Command Errors**
```python
result = subprocess.run(
    ["ls", "missing_dir"],
    capture_output=True,
    text=True
)

if result.returncode != 0:
    print("Command failed:", result.stderr)
```

### 🛠 DevOps Use Case

- Run system commands
- Trigger build or deployment steps
- Automate OS-level tasks

---

## 3️⃣ Running Remote Commands with Paramiko (SSH)

Paramiko allows Python scripts to connect to remote servers over SSH.

**🔹 Installing Paramiko**
```python
pip install paramiko
```

**🔹 SSH Command Execution**
```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname="remote-server",
    username="user",
    password="password"
)

stdin, stdout, stderr = ssh.exec_command("uptime")
print(stdout.read().decode())

ssh.close()
```

### 🛠 DevOps Use Case

- Manage remote servers
- Run commands across environments
- Automate maintenance tasks

---

## 4️⃣ Working with REST APIs using requests

REST APIs are commonly used to interact with:
- Cloud providers
- Monitoring tools
- CI/CD platforms
- Internal services

**🔹 Making a GET Request**
```python
import requests

response = requests.get("https://api.example.com/status")

print(response.status_code)
print(response.json())
```

**🔹 Handling API Errors**
```python
if response.status_code != 200:
    print("API request failed")
```

**🔹 Sending Data (POST Request)**
```python
data = {"service": "web", "status": "active"}

response = requests.post(
    "https://api.example.com/update",
    json=data
)
```

### 🛠 DevOps Use Case

- Query cloud resources
- Trigger pipelines
- Fetch monitoring data

---

## 5️⃣ Parsing and Handling JSON Data

API responses are often in JSON format.

**🔹 Parsing JSON Response**
```python
data = response.json()

service_status = data.get("status")
print(service_status)
```

**🔹 Looping Through JSON Data**
```python
for item in data.get("services", []):
    print(item["name"], item["state"])
```

**🛠 DevOps Use Case**

- Analyze API responses
- Make decisions based on data
- Automate workflows dynamically

---

## 🚀 Project: API-Driven Automation Script

**📌 Project Description**

Create a Python automation script that:
- Pulls data from a REST API
- Parses the response
- Executes system or remote commands based on conditions

**🔹 Example Workflow**

- Call an API to get service status
- Parse JSON response
- If service is down:
  - Restart service
  - Log the action
  - Notify via output

**🔹 Sample Logic**

```python
import requests
import subprocess

response = requests.get("https://api.example.com/service")

if response.status_code == 200:
    data = response.json()
    if data.get("status") == "down":
        subprocess.run(["systemctl", "restart", "service-name"])
        print("Service restarted")
```
---

## 🎯 Learning Outcomes

- Combine APIs, JSON, and system automation
- Build decision-driven scripts
- Apply Python in real DevOps workflows

---
