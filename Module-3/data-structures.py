# 1. Lists, tuples, sets, and dictionaries

# Lists - Mutable (can be changed) , ordered 

servers = ["web-1","web-2","web-3"] # list of 3 web servers
servers[2] = "db-1"

item = input("Enter new server name:")
servers.append(item)
print(servers)

# List - adding item to list, accessing single element and accessing all elements using for loop
for server in servers:
    print("Tracking server ", server)
    
# tuples - Immutable (can't be changed), ordered items like a list
ports = (8080,27017,22)
for port in ports:
    print("Port number is ", port)

# Sets - Duplicates are removed, only unique values are allowed.

ip_address = { "192.168.1.1", "192.168.2.2", "192.168.1.3"}

for ip_instance in ip_address:
    print("Server IP is ", ip_instance)

ip_address.add("192.168.1.5");
print(ip_address)

# Dictionaries - Key-value pairs, Curly braces

server_info = {
    "server-name":"web-1",
    "server-ip":"192.168.1.2",
    "status":"Running",
    "cpu":8
} 

print(server_info["server-ip"])
server_info["server-ip"]="192.168.2.2"
server_info["status"]="Stopped"
server_info["cpu"]=16

print(server_info)

for key, value in server_info.items():
    print(f"{key} : {value}")