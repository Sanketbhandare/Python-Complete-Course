# Exception handling (try, except, finally) 

import os
import shutil

source_dir = "data"
dest_dir = "backup"
checks = False

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

try:
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        dest_file = os.path.join(dest_dir, file_name)
        
        if os.path.isfile(source_file):
            shutil.copy(source_file, dest_file)
            
except FileNotFoundError:
    print("Source dir not found")
    checks = True
    
except PermissionError:
    print("Permission denied while copying files")
    checks = True
    
except Exception as e:
    print("Unexpected error: ", e)
    checks = True
    
finally:
    if not checks:
        print("File Backup done successfully.")    
    else:
        print("File Backup Failed.")    