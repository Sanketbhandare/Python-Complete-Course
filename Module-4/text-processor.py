# Text file processing

# Built-in function -> open() to interact with files
# File Modes: 1. Read , 2. Write(Overwrite), 3. Append
# with statement -> While working with files, which closes your files automatically.

note = "\nBackup is completed successfully"

with open("backup-log.txt","w+",newline="") as file:
    file.write(note)
    file.seek(0)
    content = file.read()
    print(content)
