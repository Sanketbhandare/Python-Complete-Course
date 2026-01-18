# Loops - used to repeat the tasks

import backup
# List of servers
servers = ["web-1","web-2","web-3"]

for server in servers:
    print(f" Tracking {server} for auto-healing failed services")
    # write lines of code to perform some automation on this server
    backup.backup(server)

# Modules - Scripts in the Python to avoid repeatation of code