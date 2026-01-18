import paramiko

hostname = "127.0.0.1"
userName = "vagrant"
passWord = "vagrant"
vm_port = 2222

def ssh_login(hostname, username, password, vm_port):    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=hostname, username=userName, password=passWord, port=vm_port)
        print("Login Successful")
        user_command = "uptime -p"
        print("Running User Command >>> uptime -p  <<<")
        stdin, stdout, stderr = ssh.exec_command(command=user_command)
        output = stdout.read().decode()
        print(f"Output of command is given below: \n",output)
    except:
        print("Login failed")

ssh_login(hostname, userName, passWord, vm_port)