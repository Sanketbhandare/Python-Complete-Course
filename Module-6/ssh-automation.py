import paramiko

def ssh_login(host, username, password, vm_port):    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try: 
        VM_IP = "127.0.0.1"
        username = "vagrant"
        password  = "vagrant"

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=VM_IP,username=username,password=password,port=2222)
        print("Successfully connected to VM")
    except Exception as e:
        print("Login failed \n", e)

host = "127.0.0.1"
userName = "vagrant"
passWord = "vagrant"
vm_port = "2222"

ssh_login(host, userName, passWord, vm_port)