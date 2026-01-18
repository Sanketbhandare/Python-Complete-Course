# Automation concepts for DevOps

# collect data -> analyze -> action -> log all stuff for debugging & tracking

import paramiko

# port 22 - SSH --> 2222 for this host - Port forwarding
VM_IP = "127.0.0.1"
username = "vagrant"
password  = "vagrant"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=VM_IP,username=username,password=password,port=2222)
print("Successfully connected to VM")

stdin, stdout, stderr = ssh.exec_command("df -h")

output = stdout.read().decode()
error = stderr.read().decode()

if error:
    print("Error: ", error)
else:
    print("\nDisk Usage: \n", output)


# Perform automation to check Disk space for Mount points greater than 40% utilization