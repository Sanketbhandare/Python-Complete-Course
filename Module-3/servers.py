# 4. Data handling for automation tasks

# List of dictionary
servers = [ 
        {"name":"web-1", "cpu": 55},
        {"name":"web-2", "cpu": 85},
        {"name":"web-3", "cpu": 66}   
    ]

for server in servers:
    if server["cpu"] > 60:
        print(f"Server {server['name']} has high CPU utilization of {server['cpu']}")