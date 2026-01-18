import os
import shutil

source_dir = "data"
dest_dir = "backup"

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for file_name in os.listdir(source_dir):
    source_file = os.path.join(source_dir, file_name)
    dest_file = os.path.join(dest_dir, file_name)
    
    if os.path.isfile(source_file):
        shutil.copy(source_file, dest_file)

print("File Backup done successfully.")    