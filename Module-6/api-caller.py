# Problem Statement : Create an automation script that pulls data from an API and triggers system tasks

import paramiko
import subprocess


from rest_api_demo import run_api

def login_to_vm():
    # port 22 - SSH --> 2222 for this host - Port forwarding
    VM_IP = "127.0.0.1"
    username = "vagrant"
    password  = "vagrant"
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=VM_IP, username=username, password=password, port=2222)
    print("Successfully connected to VM") 
    return ssh    

def run_commands(operation_message, command):
    ssh = login_to_vm()
    print(f"We are running {ssh}")
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    error = stderr.read().decode()
   # print("Output of command is ", output)
    exit_status = stdout.channel.recv_exit_status()
    
    if error:
        print("Error: ", error)
        return exit_status
    else:
        print(f"\n{ operation_message } ", output) 
        return exit_status

def api_caller():
    url = "https://jsonplaceholder.typicode.com/comments?postId=1"
    status_code = run_api(url)
    print("\n Status code : ", status_code)
    if status_code == 200:
        command = "sudo service cron status"
        operation_message = "Restarting cron service as below: \n"
        
        run_commands(operation_message, command)
    else:
        print("API Call Failed")

def handle_docker_action(option):
    image_name=input("Enter Docker image name: ")
    match option:
            case "1":  # Pull image
                command = f"sudo docker pull {image_name} >/dev/null 2>&1"
                exit_status = run_commands(f"Pulling docker image {image_name}", command)
                print(f"Successfully Pulled image {image_name}" if exit_status == 0 else f"Failed pulling image {image_name}")
            case "2":
                command = f"sudo docker start {image_name}"
                exit_status = run_commands(f"Starting docker container for {image_name}", command)
                print(f"Successfully Started image {image_name}" if exit_status == 0 else f"Failed starting docker image {image_name}")
            case "3":
                command = f"sudo docker stop {image_name}"
                exit_status = run_commands(f"Stopping docker container for {image_name}", command)
                print(f"Successfully Stopped Container {image_name}" if exit_status == 0 else f"Failed Stopping Container {image_name}")
            case "4":
                command = f"sudo docker image inspect {image_name} >/dev/null 2>&1"
                exit_status = run_commands(f"Checking docker image {image_name}", command)
                print(f"Docker image {image_name} is present" if exit_status == 0 else f"Docker image {image_name} is NOT PRESENT")
            case "5":
                command = f"sudo docker ps"
                exit_status = run_commands(f"Checking running docker container for {image_name}", command)
                print(f"container running for {image_name}" if exit_status == 0 else f"container NOT running for {image_name}")
            case _:
                return False  # Invalid option → exit loop                 
    return True

def docker_caller():
    while True:
        print("\n--- Docker Automation Menu ---")
        print("1. Pull Docker image ")
        print("2. Start Docker container ")
        print("3. Stop Docker container ")
        print("4. Check if Docker image  exists")
        print("5. Check running Docker containers")
        print("Enter any other key to exit")

        user_option = input("Choose an option: ").strip()
        if not handle_docker_action(user_option):
            print("Exiting menu. Goodbye!")
            break

# --- Run the menu ---
if __name__ == "__main__":
    docker_caller()   
