# Logging and basic debugging

# print() not recommanded at all for logging

import logging
import os
import shutil

logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


source_dir = "data"
dest_dir = "backup"
checks = False

try:
    logging.info("Backup has been started")

    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        dest_file = os.path.join(dest_dir, file_name)
        
        if os.path.isfile(source_file):
            shutil.copy(source_file, dest_file)
            logging.info(f"File {source_file} has been copied to backup directory at {dest_file}")
                        
except FileNotFoundError:
    logging.exception("Source dir not found")
    checks = True
    
except PermissionError:
    logging.exception("Permission denied while copying files")
    checks = True
    
except Exception as e:
    logging.exception("Unexpected error: ", e)
    checks = True
    
finally:
    if not checks:
        logging.info("File Backup done successfully.")    
    else:
        logging.error("File Backup Failed.")    