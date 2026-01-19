# Module 2: Control Flow, Functions & Core Logic 🧠🐍

This module focuses on **core programming logic in Python**.  
It teaches how programs make decisions, repeat tasks, and organize logic using functions.  
These concepts are **essential for DevOps automation**, scripting, and infrastructure tooling.

---

## 🎯 Module Goals

By completing this module, you will be able to:
- Write Python programs with logical flow
- Make decisions using conditions
- Automate repetitive tasks using loops
- Create reusable and modular functions
- Build a small real-world project using core Python concepts

---

## 1️⃣ Basic Syntax, Variables & Data Types

Python programs are built using variables and data types.

### 🔹 Variables
Variables store data in memory.

```python
name = "DevOps Engineer"
age = 25
is_active = True
```

🔹 Common Data Types
| Data Type |	Example|
|---|---|
|int|	10|
|float|	3.14|
|str|	"Python"|
|bool|	True / False|

**Example:**
```python
cpu_cores = 4
memory_gb = 16.5
cloud_provider = "AWS"
is_running = True
```

**🔹 Type Checking**
```python
print(type(cpu_cores))      # <class 'int'>
print(type(cloud_provider)) # <class 'str'>
```

**🛠 DevOps Use Case**
- Store environment values
- Handle configuration parameters
- Process user input and script arguments

## 2️⃣ Conditional Statements (if, else, elif)
Conditional statements control decision-making in programs.

🔹 Basic if Statement
```python
cpu_usage = 85

if cpu_usage > 80:
    print("High CPU usage")
```

🔹 if-else
```python
disk_space = 40

if disk_space < 20:
    print("Low disk space")
else:
    print("Disk space is sufficient")
```

🔹 if-elif-else
```python
status_code = 200

if status_code == 200:
    print("Success")
elif status_code == 404:
    print("Not Found")
else:
    print("Server Error")
```

**🛠 DevOps Use Case**
- Check deployment success or failure
- Validate server health
- Handle different execution paths in scripts

## 3️⃣ Loops (for, while)

Loops help automate repetitive tasks.

🔁 for Loop
Used when the number of iterations is known.
```python
servers = ["server1", "server2", "server3"]

for server in servers:
    print(f"Connecting to {server}")
```

🔁 range() with for
```python
for i in range(5):
    print(i)
```

🔄 while Loop

Used when the condition controls execution.
```python
attempts = 0

while attempts < 3:
    print("Retrying connection...")
    attempts += 1
```

🔹 Loop Control Keywords
```python
for i in range(10):
    if i == 5:
        break   # stops the loop
    print(i)

for i in range(5):
    if i == 2:
        continue  # skips this iteration
    print(i)
```

**🛠 DevOps Use Case**
- Run commands on multiple servers
- Retry failed operations
- Process files, logs, or resources

## 4️⃣ Functions & Lambda Expressions

Functions allow you to reuse logic and keep code clean.

🔹 Defining a Function
```python
def greet(name):
    print(f"Hello, {name}")
```

🔹 Calling a Function
```python
greet("DevOps Engineer")
```

🔹 Function with Return Value
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

🔹 Default Arguments
```python
def deploy(env="dev"):
    print(f"Deploying to {env} environment")

deploy()
deploy("production")
```

🔹 Lambda Functions

Small one-line functions.
```python
square = lambda x: x * x
print(square(4))
```

**🛠 DevOps Use Case**
- Utility functions for scripts
- Code reuse in automation tools
- Cleaner and maintainable codebases

## 5️⃣ Writing Reusable & Modular Code

Reusable code is:
- Easier to maintain
- Easier to test
- Scales well in large projects

❌ Bad Practice (Repeated Code)
```python
print("Connecting to server")
print("Running command")
```

✅ Good Practice (Reusable Function)
```python
def run_task():
    print("Connecting to server")
    print("Running command")

run_task()
```

🧱 Modular Thinking
Break programs into:
- Small functions
- Logical steps
- Clear responsibilities

**🛠 DevOps Use Case**
- Build reusable automation scripts
- Maintain CI/CD pipelines
- Organize infrastructure tools

---

## 🚀 Project: Create a Calculator**

**📌 Project Description**
A command-line calculator that performs basic arithmetic operations.

### 🔢 Supported Operations
- Addition
- Subtraction
- Multiplication
- Division

**🧩 Example Logic**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

choice = input("Enter operation (+, -, *, /): ")

if choice == "+":
    print(add(10, 5))
elif choice == "-":
    print(subtract(10, 5))
```
---

## 🎯 Learning Outcomes
- Combine functions, conditions, and loops
- Handle user input
- Build a real, working program
- Strengthen problem-solving skills

---
