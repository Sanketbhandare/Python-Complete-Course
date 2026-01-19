# Module 3: Python Data Structures 🧺🐍

This module introduces Python data structures, which are essential for storing, organizing, and processing data efficiently.
In DevOps, data structures are heavily used for log analysis, configuration management, automation scripts, and cloud resource handling.

## 🎯 Module Goals

By the end of this module, you will be able to:
- Use Python data structures effectively
- Perform common operations on collections
- Write efficient code using list comprehensions
- Process structured and unstructured data
- Build an automation-focused mini project using data structures

---

## 1️⃣ Lists, Tuples, Sets, and Dictionaries

Python provides multiple built-in data structures, each with specific use cases.

### 🔹 Lists

Lists are ordered, mutable collections.
```python
servers = ["web-1", "web-2", "db-1"]
servers.append("cache-1")
print(servers)
```

**Use Cases:**
- Store server names
- Maintain task lists
- Handle collections of resources
---

### 🔹 Tuples

Tuples are ordered and immutable.

```python
region = ("us-east-1", "aws")
print(region[0])
```

**Use Cases:**
- Store fixed configuration values
- Protect data from modification
---

### 🔹 Sets

Sets store unique, unordered elements.

```python
ip_addresses = {"10.0.0.1", "10.0.0.2", "10.0.0.1"}
print(ip_addresses)
```

**Use Cases:**
- Remove duplicates
- Track unique resources or IPs
---

### 🔹 Dictionaries

Dictionaries store key–value pairs.

```python
server_info = {
    "name": "web-1",
    "status": "running",
    "cpu": 70
}
print(server_info["status"])
```

**Use Cases:**
- Configuration data
- JSON-like structures
- Cloud resource metadata

---

## 2️⃣ Common Operations and Methods

Each data structure supports useful operations and built-in methods.

### 🔹 List Operations

```python
numbers = [1, 2, 3, 4]
numbers.insert(1, 10)
numbers.remove(3)
print(numbers)
```

**Common methods:**
- append()
- insert()
- remove()
- pop()
- sort()

### 🔹 Dictionary Operations

```python
config = {"env": "prod", "version": "1.0"}
config["region"] = "us-east-1"
print(config.keys())
print(config.values())
```

**Common methods:**
- keys()
- values()
- items()
- get()

### 🔹 Set Operations
```python
a = {"server1", "server2"}
b = {"server2", "server3"}

print(a.union(b))
print(a.intersection(b))
```

### 🛠 DevOps Use Case
- Manage cloud resource data
- Modify deployment configurations
- Process API responses

---

## 3️⃣ List Comprehensions for Efficiency

List comprehensions provide a compact and readable way to create lists.


**🔹 Basic Example**
```python
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)
```

🔹 With Conditions
```python
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)
```

### 🛠 DevOps Use Case
- Filter active servers
- Transform log data
- Clean and preprocess datasets

---

## 4️⃣ Data Handling for Automation Tasks

Data structures are commonly used to process automation data such as logs, configs, and metrics.

**🔹 Example: Parsing Log Levels**
```python
logs = [
    "INFO Service started",
    "ERROR Database connection failed",
    "WARNING Disk space low"
]

errors = [log for log in logs if "ERROR" in log]
print(errors)
```

**🔹 Example: Counting Occurrences**
```python
status_codes = [200, 500, 200, 404, 500, 200]

summary = {}
for code in status_codes:
    summary[code] = summary.get(code, 0) + 1

print(summary)
```

### 🛠 DevOps Use Case
- Analyze logs
- Aggregate metrics
- Generate reports automatically

---

## 🚀 Project: Build a Log Analyzer

**📌 Project Description:** 

Build a Python script that:
  - Reads log data
  - Parses relevant information
  - Generates a summary using Python data structures

## 🔍 Features
- Identify log levels (INFO, WARNING, ERROR)
- Count occurrences
- Display summarized output

**🧩 Sample Logic**
```python
log_data = [
    "INFO App started",
    "ERROR Connection failed",
    "INFO Request processed",
    "ERROR Timeout occurred"
]

log_summary = {}

for log in log_data:
    level = log.split()[0]
    log_summary[level] = log_summary.get(level, 0) + 1

print(log_summary)
```
---

## 🎯 Learning Outcomes

- Apply data structures in real-world scenarios
- Process and summarize data
- Strengthen automation skills
- Prepare for DevOps scripting tasks

---
