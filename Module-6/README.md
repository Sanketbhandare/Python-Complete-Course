# Module 6: DevOps Automation with Python 🚀🐍⚙️

This module brings together everything learned so far to build real-world DevOps automation workflows using Python.
You will automate remote server access, Docker container management, and secure credential handling, simulating production-grade DevOps tools.

## 🎯 Module Goals

By the end of this module, you will be able to:
- Automate remote servers using SSH
- Manage Docker containers programmatically
- Apply basic security best practices
- Combine multiple tools into complete automation workflows
- Build an end-to-end DevOps automation tool

---

## 1️⃣ SSH Automation Using Paramiko

SSH automation is essential for managing remote servers.

**🔹 Establishing an SSH Connection**

```python
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname="server-ip",
    username="user",
    key_filename="~/.ssh/id_rsa"
)
```

**🔹 Executing Remote Commands**
```python
stdin, stdout, stderr = ssh.exec_command("df -h")
print(stdout.read().decode())
```

**🔹 Handling Errors**
```python
error = stderr.read().decode()
if error:
    print("Error:", error)
```

### 🛠 DevOps Use Case

- Remote server monitoring
- Service restarts
- Infrastructure maintenance

---

## 2️⃣ Docker Automation Using Python

Python can interact with Docker using the Docker SDK.

> NOTE: For given project in this module, we have used native Linux commands for Docker instead of docker Python module.
 
**🔹 Installing Docker SDK**
```python
pip install docker
```

**🔹 Connecting to Docker**
```python
import docker

client = docker.from_env()
```

**🔹 Listing Containers**
```python
containers = client.containers.list(all=True)

for container in containers:
    print(container.name, container.status)
```

**🔹 Starting and Stopping Containers**
```python
container = client.containers.get("web_app")
container.start()
container.stop()
```

### 🛠 DevOps Use Case

- Manage application containers
- Automate deployments
- Control container lifecycles

---

## 3️⃣ Basic Security Practices

Handling secrets securely is critical in DevOps.

**🔹 Using Environment Variables**
```python
import os

api_key = os.getenv("API_KEY")
```

**🔹 Avoid Hardcoding Secrets**

**❌ Bad Practice:**
```python
password = "mypassword"
```

**✅ Good Practice:**
```python
password = os.getenv("DB_PASSWORD")
```

**🔹 .env File Usage**

```python
API_KEY=your_api_key_here
DB_PASSWORD=your_password_here
```

### 🛠 DevOps Use Case

- Secure API access
- Safe credential management
- Compliance with best practices

---

## 4️⃣ Putting Everything Together: Real Workflows

Real DevOps automation combines multiple tools and steps.

**🔹 Example Workflow**

- Connect to a remote server via SSH
- Check system status
- Manage Docker containers
- Log actions and handle errors

**🔹 Sample Integrated Logic**

```python
import paramiko
import docker

# SSH connection
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("server-ip", username="user", key_filename="~/.ssh/id_rsa")

# Run remote command
stdin, stdout, stderr = ssh.exec_command("docker ps")
print(stdout.read().decode())

# Docker management
client = docker.from_env()
for container in client.containers.list():
    print(container.name)

ssh.close()
```

### 🛠 DevOps Use Case

- Full-stack automation tools
- Remote container orchestration
- Production operations scripting

---

## 🚀 Project: End-to-End DevOps Automation Tool

**📌 Project Description**

Build a Python-based DevOps automation tool that:
- Connects to a remote server using SSH
- Manages Docker containers
- Applies secure credential handling
- Performs multiple automated tasks in sequence

> NOTE: Please refer Project code given in this module for your reference.

**🔧 Project Features**

- SSH-based remote command execution
- List, start, stop Docker containers
- Environment-based secret management
- Error handling and logging

---

## 🎯 Learning Outcomes

- Build production-ready DevOps automation
- Combine multiple Python libraries
- Apply security best practices
- Simulate real-world DevOps workflows

---
