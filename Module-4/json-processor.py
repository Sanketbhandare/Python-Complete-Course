import json
from datetime import datetime

config_data = {
    "source_dir": "data",
    "backup_dir": "backup",
    "runs": []
}

with open("backup-config.json","w") as file:
    json.dump(config_data, file, indent=4)

print("Backup Config data file has been created.")

with open("backup-config.json","r") as file:
    config = json.load(file)

run_info = {
        "time": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
        "status": "Success"
    } 

config["runs"].append(run_info)

with open("backup-config.json","w") as file:
    config = json.dump(config, file, indent=4)

print("Backup Run info updated in JSON")    

with open("backup-config.json","r") as file:
    config = json.load(file)
    
for run in config["runs"]:
    print(run)